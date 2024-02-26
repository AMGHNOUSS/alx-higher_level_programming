import cmd

class HelloWorld(cmd.Cmd):
    """Simple command processor example."""
    FRIENDS = [ 'Alice', 'Adam', 'Barbara', 'Bob' ]

    def do_greet(self, person):
        if person and person in self.FRIENDS:
            greeting = 'hi, %s!' % person
        elif person:
            greeting = "hello, " + person
        else:
            greeting = 'hello'
        print (greeting)
    
    def do_EOF(self):
        return True
    
    def help_greet(self):
        print('\n'.join([ 'greet [person]',
                           'Greet the named person',
                           ]))
        
    def do_help(self, line):
        print("Undocumented commands:")
        print("=====================")
        print("help    greet    EOF")
    
    
if __name__ == '__main__':
    HelloWorld().cmdloop()