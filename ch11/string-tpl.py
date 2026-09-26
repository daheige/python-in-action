from string import Template

t = Template("${village}folk send $$10 to $cause.")
s = t.substitute(village="Nottingham", cause="the ditch fund")
print(s)
