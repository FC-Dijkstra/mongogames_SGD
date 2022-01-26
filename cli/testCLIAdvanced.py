import cmd
from operator import truediv


class CLIAdvanced(cmd.Cmd):
    intro = "La CLI avancée de test (help pour de l'aide"

    ruler = "*"
    doc_header = "Aide sur les commandes (help <cmd>)"
    misc_header = "Commandes diverses"
    undoc_header = "Commandes non documentées"

    prompt = ">"
    distributions = {
        "Debian": "Debian stretch 9.2",
        "Ubuntu": "Ubuntu Kylin 17.04",
        "CentOS": "CentOS 7.4"
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.advancedMode = False
        self.prompt = CLIAdvanced.prompt

    def do_quit(self, line):
        """Quitte l'interface"""
        print("Adieu")
        exit(0)

    def do_lastVersion(self, name):
        """Display last version of [distribution]"""
        if name:
            if name in CLIAdvanced.distributions:
                print(CLIAdvanced.distributions[name])
            else:
                print("Version inconnue")
        else:
            print("Vous devez spécifier le nom d'une distribution")

    def complete_lastVersion(self, text, line, start_index, end_index):
        if text:
            return [
                name for name in CLIAdvanced.distributions
                if name.startswith(text)
            ]
        else:
            return list(CLIAdvanced.distributions.keys())

    def do_advanced(self, text):
        """Passage en mode avancé"""
        if not text:
            if self.advancedMode:
                print("Déjà en mode avancé")
            else:
                self.advancedMode = True
                self.prompt = "[ADVANCED]" + CLIAdvanced.prompt
        else:
            print("Aucun paramètre requis pour cette commande")

    def do_normal(self, text):
        """Passage en mode normal"""
        if not text:
            if self.advancedMode:
                self.advancedMode = False
                self.prompt = CLIAdvanced.prompt
            else:
                print("Déjà en mode normal")
        else:
            print("Aucun paramètre requis pour cette commande")

    def do_imTheBoss(self, text):
        """Commande en mode avancé"""
        if not self.advancedMode:
            print("Vous devez être en mode avancé pour lancer cette commande")
        else:
            if text:
                print("Aucun paramètre requis pour cette commande")
            else:
                print("OK you are the boss")


if __name__ == "__main__":
    cli = CLIAdvanced()
    cli.cmdloop()
