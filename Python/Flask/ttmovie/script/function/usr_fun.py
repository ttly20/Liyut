#  coding utf-8

"""
method:_passMi()
 Prototype method:
 def _passMi(self, string)
 This method is used to do password encryption, it will perform a 128-bit custom encryption algorithm
"""
import Database
import string


class usr_fun:
    
    def _passMi(self, string):
        # This method is used to do password encryption, it w-
        # ill perform a 128-bit custom encryption algorithm
        char = ["a", "b", "c", "d", "e", "f","g", "h",
                "i", "j", "k", "l", "m", "n", "o", "p",
                "q", "r", "s", "t", "u", "v", "w", "x",
                "y", "z", "A", "B", "C", "D", "E", "F",
                "G", "H", "I", "J", "K", "L", "M", "N",
                "O", "P", "Q", "R", "S", "T", "U", "V",
                "W", "X", "Y", "Z", "1", "2", "3", "4",
                "5", "6", "7", "8", "9", "0", "`", "~",
                "!", "@", "#", "$", "%", "^", "&", "*",
                "(", ")", "-", "_", "=", "+", "[", "{",
                "]", "}", "\\", "|", ";", ":", "'", "\'",
                ",", "<", ".", ">", "/", "?"]
        char_mi = ["`", "1", "2", "3", "4", "5", "6", "7", "8",
                   "9", "0", "-", "=", "~", "!", "@", "#", "$",
                   "%", "^", "&", "*", "(", ")", "_", "+", "q",
                   "w", "e", "r", "t", "y", "u", "i", "o", "p",
                   "[", "]", "\\", "Q", "W", "E", "R", "T", "Y",
                   "U", "I", "O", "P", "{", "}", "|", "a", "s",
                   "d", "f", "g", "h", "j", "k", "l", ";", "'",
                   "A", "S", "D", "F", "G", "H", "J", "K", "L",
                   ":", "\"", "z", "x", "c", "v", "b", "n", "m",
                   ",", ".", "/", "Z", "X", "C", "V", "B", "N",
                   "M", "<", ">", "?"]
        passstr = list(string)
        passmi = []
        tmppass = []
        passadre = []
        passlen = 0
        for iterm in passstr:
            passadre.append(char.index(iterm))
        for num in passadre:
            tmppass.append(char_mi(num))
        passlen = len(passstr)
        milen = (128 - passlen) / passlen
        bulen = (128 - passlen) - milen*passlen
        for tmp in tmppass:
            passmi.append(tmp)
            for mi in (0, milen):
                passmi.append(char_mi[mi])
        if bulen > 0:
            for bu in (1, bulen):
                passmi.append(char_mi[bu-1])
        return str(passmi)
