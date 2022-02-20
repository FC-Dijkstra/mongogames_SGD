import cmd


class CLISimple(cmd.Cmd):
    intro = "La CLI du projet. (help pour de l\'aide)"
    prompt = "~>"

    distributions = {
        "Debian": "Debian stretch 9.2",
        "Ubuntu": "Ubuntu Kylin 17.04",
        "CentOS": "CentOS 7.4"
    }

    def do_quit(self, line):
        """Quitte l'interface"""
        print("Au revoir")
        exit(0)

    def do_lastVersion(self, name):
        if name:
            if name in CLISimple.distributions:
                print(CLISimple.distributions[name])
            else:
                print("Version inconnue")
        else:
            print("Vous devez spécifier le nom d'une distribution")

    def complete_lastVersion(self, text, line, start_index, end_index):
        if text:
            return [
                name for name in CLISimple.distributions
                if name.startswith(text)
            ]
        else:
            return list(CLISimple.distributions.keys())


if __name__ == "__main__":
    cli = CLISimple()
    cli.cmdloop()
