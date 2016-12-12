import args_checker
import capturer
import outputer
import readin
import sys
if __name__ == "__main__":
    args = args_checker.Args_checker(sys.argv)
    rea = readin.Readin(args)
    capt = capturer.Capturer(rea)
    outp = outputer.Outputer(capt)
