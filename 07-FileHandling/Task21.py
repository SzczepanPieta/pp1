fn = open('07-FileHandling/random.txt', 'r')
  
fn1 = open('07-FileHandling/copy.txt', 'w')
  
cont = fn.readlines()
type(cont)
for i in range(0, len(cont)):
    fn1.write(cont[i])

fn1.close()
fn.close()
