output = ''
reserves = []
nonterminals = []
terminals= []
andix = 0
final = []
final1 = []
newnonterminals = []
help1 = []
help2= []
finalstep = []
temp = []
a = []
z = []
i = 1
j = 1
k = 0
initial = ''
tops = ''
first = True
newrhs = ''
new = ''
rule = ''
sss = ''

rule_map = {}       # stores rules

# Returns a string representation
# of the given rule
def stringify(rule):
    string = rule[0] + ' ->'
    for item in rule[1:]:
        string += ' ' + item
    
    
    return string


# Adds a rule to the dictionary of rules
def add_rule(rule):
    
    global rule_map
    
    if rule[0] not in rule_map:
        rule_map[rule[0]] = []
    rule_map[rule[0]].append(rule[1:])

#open('grammar rule.txt') for finding nonterminals
f = open ('grammar rule.txt' , 'r')

while True:
    line = f.readline()
    
    if line == '':
        break
    line = line.strip()

    # do not process commented or empty lines
    if line != '' and line[0] != '#':

        line = line.strip().split(' -> ')
        if first:
           initial = line[0]
           first = False
           nonterminals.append(initial)
        for item in nonterminals:
           if line[0] != item :
              if line[0] not in nonterminals: 
                 nonterminals.append(line[0])
#print nonterminals

#open('grammar rule.txt') for finding terminals
f = open ('grammar rule.txt' , 'r')
while True:
    line = f.readline()
    
    if line == '':
        break
    line = line.strip()
   # print line

    # do not process commented or empty lines
    if line != '' and line[0] != '#':

        line = line.strip().split(' -> ')
       # print line
        lhs = line[0].strip()
      #  print lhs

        rhs = line[1:][0].strip('.').split()
       # print rhs
        for item in rhs:
           if item not in nonterminals:
               if item not in terminals:
                terminals.append(item)
#print terminals

# add new rules to the grammer         
for item in terminals:
  new_node = 'X' + str(j)
  if new_node not in newnonterminals:
        newnonterminals.append (new_node)
        final.append(new_node+ ' -> '+item)
        help1.append (item)
        help2.append (new_node)
        j = j + 1

#open('grammar rule.txt') for processing
f = open ('grammar rule.txt' , 'r')
while True:
    line = f.readline()
    
    if line == '':
        break
    line = line.strip()
 
    # do not process commented or empty lines
    if line != '' and line[0] != '#':

        rule = line
        line = line.strip('.').split(' -> ')
       
        rhs = line[1:][0].strip('.').split()
       
       # reserve unit productions for the end
        if len(rhs)==1:
             for item in rhs:
                if item not in terminals:
                   reserves.append(line)
                else:
                   final1.append(line[0]+ ' -> '+line[1])

        elif len(rhs) > 1:
             for item in rhs:
                 if item in terminals:
                       andix = terminals.index(item)
                       for har in help2:
                            if help2.index(har) == andix:
                                new = har
                                a = rule.split(' ')
                                
                                rule = rule.replace(' '+item , ' '+new)
                                
             finalstep.append(rule)
             rule = rule.split(' ')
        
             while len(rule) > 4:
                 new_node = 'X' + str(j)
                 sss = rule[0] + ' -> ' + rule[2] + ' ' + new_node 
                
                 temp.append(sss)
                
                 rule = [new_node] + ['->'] + rule[3:]
                 j =  j + 1
         
             sss = rule[0] + ' -> ' + rule[2] + ' ' + rule[3]
             temp.append(sss)

        
for d in temp:
    final.append (d)
    
for f in final1:
    final.append (f)

for y in final:
  y = y.strip().split(' -> ')

  z.append (y[0])

for u in reserves:
    add_rule(u)

for t in final:
    t = t.strip().split(' -> ')
    add_rule(t)
#print rule_map

while len(reserves) > 0:
    rule = reserves.pop()
    if rule[1] in rule_map:
        
        for item in rule_map[rule[1]]:
                new_rule = [rule[0]] + item
                
                # if not a unit production anymore, output
                if len(new_rule) > 2 or new_rule[1][0] in terminals:
                        output += stringify(new_rule)
                
                # still a unit production, recycle
                else:
                    reserves.append(new_rule)
                    
                add_rule(new_rule)
                final.append (stringify(new_rule))
m = open ('cnf.txt' , 'w')
for l in final:  
    
    m.write (l)
    m.write ("\n")
m.close()
