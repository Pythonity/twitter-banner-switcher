import os
import random

import yaml
import click
import tweepy


@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.option('--config-file', '-c', type=click.File(),
              default=os.path.join(os.path.expanduser('~'),
                                   '.twitter-banner-switcher.yml'),
              help="Path to YAML config file (default: "
                   "~/.twitter-banner-switcher.yml).")
def cli(config_file):
    """
    Set Twitter profile banner to a random image from a specified folder
    or a list of paths
    """
    config = _get_config(config_file)

    try:
        auth = tweepy.OAuthHandler(
            config['consumer_key'], config['consumer_secret']
        )
        auth.set_access_token(
            config['access_token'], config['access_token_secret']
        )

        api = tweepy.API(auth)
    except Exception as e:
        raise click.ClickException(repr(e))

    image = random.choice(config['banner_images'])

    try:
        api.update_profile_banner(image)
    except Exception as e:
        raise click.ClickException(repr(e))

    click.secho(
        "Twitter background successfully changed to '{}'".format(image),
        fg='green'
    )


def _get_config(yaml_file):
    """Parse YAML config file"""
    VALID_EXTENSIONS = ['.gif', '.jpg', '.jpeg', '.png']
    config = yaml.safe_load(yaml_file)

    # If only one path is provided, convert it to list
    if isinstance(config['banner_images'], str):
        banner_images_paths = [config['banner_images']]
    else:
        banner_images_paths = config['banner_images']

    banner_images = list()
    for p in banner_images_paths:
        if (os.path.isfile(p) and
                os.path.splitext(p)[1].lower() in VALID_EXTENSIONS):
            banner_images.append(p)
        elif os.path.isdir(p):
            images = [
                os.path.join(p, fn) for fn in os.listdir(p)
                if any(fn.endswith(ext) for ext in VALID_EXTENSIONS)
            ]
            banner_images += images

    try:
        consumer_key = config['consumer_key']
        consumer_secret = config['consumer_secret']
        access_token = config['access_token']
        access_token_secret = config['access_token_secret']

        # Make sure all values are not empty
        if not all([consumer_key, consumer_secret, access_token,
                    access_token_secret, banner_images]):
            raise ValueError
    except (TypeError, ValueError, KeyError):
        raise click.ClickException(
            "Passed YAML file doesn't have all needed values - all of "
            "'consumer_key', 'consumer_secret', 'access_token', "
            "'access_token_secret' and 'banner_images' are required."
        )

    return {
        'consumer_key': config['consumer_key'],
        'consumer_secret': config['consumer_secret'],
        'access_token': config['access_token'],
        'access_token_secret': config['access_token_secret'],
        'banner_images': banner_images,
    }

if __name__ == '__main__':
    cli()
