class Category:
    def __init__(self, category):
        self.name = category
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        balance = 0
        for l in self.ledger:
            balance += l["amount"]
        return balance

    def transfer(self, amount, categoryObject):
        if self.withdraw(amount, "Transfer to " + categoryObject.name):
            categoryObject.deposit(amount, "Transfer from " + self.name)
            return True
        return False

    def check_funds(self, amount):
        balance = self.get_balance()
        if amount > balance:
            return False
        return True

    def __str__(self):
        title = self.name.center(30, '*')
        list = ""
        for l in self.ledger:
            list += '{:<23}'.format(l['description'])[:23]
            text = '{:.2f}'.format(l['amount'])
            text = '{:>7}'.format(text)[:10]
            list += text + "\n"
        total = 'Total: ' + '{:.2f}'.format(self.get_balance())

        return (title + "\n" + list + total)


def create_spend_chart(categories):
    spent = []
    total = 0
    i=0
    for category in categories:
      partial = 0
      for l in category.ledger:
        if l['amount']<0:
          #print(str(i) + " " + str(l['amount']))
          partial += l['amount']
          total+= l['amount']
      
      
      spent.append(partial)
      i+=1
    title = 'Percentage spent by category\n'
    body = ""
    for i in range(100, -10, -10):
        strng = ""
        for index, s in enumerate(spent):
          #print(str(index) + " "+ str((s/total)*100))
          if ((s/total)*100) >i:
            strng += "o  "
          else:
            strng +="   "
        body += ((str(i) + "| ").rjust(5) + strng)+"\n"  
    body+=("    ----------\n")    
    legend=""
    names = []
    for category in categories:
        names.append(len(category.name))
    max_len = max(names)
    for i in range(max_len):
        string = "   "
        for category in categories:
          if i< len(category.name):
            string +="  " + category.name[i]
          else:
            string +="   "
        string += "  "
        legend += string
        legend += ("\n")
    return(title+body+legend.rstrip() + '  ')
    