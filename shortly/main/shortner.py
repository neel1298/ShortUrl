import string,random


class shortner():
    
    def shorturl(self,link):
        newlink = ''
        for i in link:

            if i.isalpha():
                newlink = newlink + i
        shortlink = ''.join(random.choice(newlink) for i in range(5))
        
        return shortlink
