import service
import click
import dotenv
import os

class Chatty:
    host = ''
    current_chat = ''
    token = ''

    def __init__(self):
        self.dotenv_file = dotenv.find_dotenv()
        dotenv.load_dotenv(self.dotenv_file)
        self.host = os.environ["HOST"]
        self.current_chat = os.environ['C_CHAT']
        self.token = os.environ['TOKEN']

        res = service.test_conn(self.host)
        if res != 200 and res != 404:
            raise Exception("not connected,err_code: %s" % res)

    def set_token(self,token):
        os.environ["TOKEN"] = token
        dotenv.set_key(self.dotenv_file, "TOKEN", os.environ["TOKEN"])

    def set_current_chat(self):
        ''''''
    # def set_config(self, key, value):
    #     self.config[key] = value
    #     if self.verbose:
    #         click.echo(f"  config[{key}] = {value}", file=sys.stderr)
    #
    # def __repr__(self):
    #     return f"<Repo {self.home}>"


S = Chatty()



@click.group()
def cli():
    """Repo is a command line tool that showcases how to build complex
    command line interfaces with Click.
    This tool is supposed to look like a distributed version control
    system to show how something like this can be structured.
    """
    # Create a repo object and remember it as as the context object.  From
    # this point onwards other commands can refer to it by using the
    # @pass_repo decorator.
#TODO test connection
    #S.set_connection()

    # ctx.obj = Repo(os.path.abspath(repo_home))
    # ctx.obj.verbose = verbose
    # for key, value in config:
    #     ctx.obj.set_config(key, value)


# @cli.command()
# @click.argument("src")
# @click.argument("dest", required=False)
# @click.option(
#     "--shallow/--deep",
#     default=False,
#     help="Makes a checkout shallow or deep.  Deep by default.",
# )
# @click.option(
#     "--rev", "-r", default="HEAD", help="Clone a specific revision instead of HEAD."
# )
# def clone(repo, src, dest, shallow, rev):
#     """Clones a repository.
#     This will clone the repository at SRC into the folder DEST.  If DEST
#     is not provided this will automatically use the last path component
#     of SRC and create that folder.
#     """
#     if dest is None:
#         dest = posixpath.split(src)[-1] or "."
#     click.echo(f"Cloning repo {src} to {os.path.basename(dest)}")
#     repo.home = dest
#     if shallow:
#         click.echo("Making shallow checkout")
#     click.echo(f"Checking out revision {rev}")

@cli.command()
def list():

    res = service.get_list(S.host,S.token)
    click.echo(res)


@cli.command()
@click.confirmation_option()
def delete(repo):
    """Deletes a repository.
    This will throw away the current repository.
    """
    click.echo(f"Destroying repo {repo.home}")
    click.echo("Deleted!")


@cli.command()
@click.option("--username", prompt=True, help="The username.")
@click.password_option(help="The login password.")
def login(username, password):
    """Log in.Give current credentials.
    """
    print("hello,word")
    click.echo("hello_word")
@cli.command()
@click.option("--username", prompt=True, help="The username.")
@click.option("--email", prompt="E-mail", help="The user email.")
@click.password_option(help="The login password.")
def signup(username, password,email):
    """Log in.Give current credentials.
    """
    res = service.sign_up(S.host,username,email,password)

    S.set_token(res)

    click.echo("Пользователь успешно создан")

@cli.command()
@click.option(
    "--message",
    "-m",
    multiple=True,
    required=True,
    help="The message to send chat.",
)
def message(message):
    """
    repo message -m Hello_word
    """
    click.echo(message)

@cli.command()
@click.option(
    "--name",
    "-n",
    multiple=True,
    required=True,
    help="New chat name",
)
def create(name):
    """
    This command create new chat.
    repo create -n Chat1
    """
    click.echo(name)

@cli.command()
@click.option(
    "--chat_name",
    "-c",
    multiple=True,
    required=True,
    help="Select chat",
)
def select(chat_name):
    """
    This command select req chat.
    repo select -c Chat1
    """
    res = service.select_chat(S.host,chat_name,S.token)
    click.echo(res)



@cli.command()
@click.option(
    "--leave_chat_name",
    "-l",
    multiple=True,
    required=True,
    help="Leave chat",
)
def leave(leave_chat_name):
    """
    This command leave req chat.
    repo leave -l Chat1
    """
    click.echo(leave_chat_name)

@cli.command()
def refresh():
    """
    This command refresh current chat.
    repo refresh -c Chat1
    """
    click.echo('qwe')


@cli.command()
def logout():
    S.set_token('')
    click.echo('ok')

#
# @cli.command(short_help="Copies files.")
# @click.option(
#     "--force", is_flag=True, help="forcibly copy over an existing managed file"
# )
# @click.argument("src", nargs=-1, type=click.Path())
# @click.argument("dst", type=click.Path())
# def copy(repo, src, dst, force):
#     """Copies one or multiple files to a new location.  This copies all
#     files from SRC to DST.
#     """
#     for fn in src:
#         click.echo(f"Copy from {fn} -> {dst}")