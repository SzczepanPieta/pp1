fn = open('random.txt', 'r')
  
fn1 = open('copy.txt', 'w')
  
cont = fn.readlines()
type(cont)
for i in range(0, len(cont)):
    fn1.write(cont[i])

fn1.close()
fn.close()
