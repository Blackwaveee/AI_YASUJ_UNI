import sys

class Args:
    @staticmethod
    def parse():
        args = sys.argv[1:]

        paras = {}

        for arg in args:
            status = 0
            word = ''
            val = ''
            for ch in arg:
                if status == 0:
                    if ch == '=':
                        status = 1
                    else:
                        word+=ch
                else:
                    val += ch
            paras[word] = None if val == '' else val

        return paras

class Action:
    @staticmethod
    def make(paras):
        print(paras)
        name = paras['name'] if 'name' in paras else exit()
        del paras['name']
        Action.callFile(name,paras)

    @staticmethod
    def callFile(name,paras):
        exec('from actions import '+name)
        exec(name+'.run(paras)')

Action.make(Args.parse())

