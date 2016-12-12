import  sys
import os
class Args_checker(object):

    def __checkinputfile(self,inp):
        if os.path.exists(inp):
            if os.path.isdir(inp):
                self.__checkinputfolder(inp)
            else:
                f1 = open(inp,'r')
                try:
                    f2 = f1.read(f1)
                except:
                    print("[ERROR] Can not open input file!")
                    sys.exit(1)
                finally:
                    f1.close()
        else:
            print("[ERROR]Input file or folder doesn't exist!.")
            sys.exit(1)
    def __checkinputfolder(self,inp):
        for rt,dirs,files in os.walk(inp):
            print(rt)
            print(dirs)
            print(files)
            pass

    def __checkoutputfile(self,outp):
        pass
    def __checkoutputfolder(self,outp):
        pass

    def __init__(self,args):
        self.args = args
        #check if args is list.
        if isinstance(self.args,list) == False:
            print("[ERROR]Args_checker: Input error.")
            sys.exit(1)
        if self.args.index("-h") != -1 or self.args.index("--help") != -1:
            print("-h or --help     :Show help")
            print("-f [option]      :Set input file or folder")
            print("-o [option]      :Set Output file.Default: $PWD/output.txt")
        pos = self.args.index("-f")
        if pos != -1:
            self.__checkinputfile(args[pos+1])
        else:
            print("[ERROR]Args_checker: Please Set input file or folder")
            sys.exit(1)
        pos = self.args.index("-o")
        if pos != -1:
            self.__checkoutputfile(args[pos+1])
        else:
            print("[WARNING]Args_checker:Not set output file. Using default. ")
            self.__checkoutputfile(sys.path()+"/output.txt")