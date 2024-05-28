import json

f = open("codex.svg", "r", encoding="UTF-8")

links =  []
line = f.readline()
while line:
    if "https://" in line:
        # print(line)
        ex = line.split('"')
        print(ex[1])
        links.append(ex[1])
    line = f.readline()
f.close()

print(len(links))


f = open("biases.json", "r", encoding="UTF-8")
j = json.load(f)
f.close()
F_replace = open("biases.json", "r", encoding='UTF-8')
text = F_replace.readlines()
F_replace.close()
print(text)
output = []
global_counter = 0
for i in range(0, 4):
    group = j["children"][i]["children"]
    # print(group)
    for k in range(0, len(group)):
        for l in group[k]["children"]:
            if "Bike-shedding" in l['name']:
                continue
            else:
                output.append({"name": l['name'], "link": links[global_counter]})
                global_counter+=1

for el in output:
    for k in range(0, len(text)):
        if el['name'] in text[k]:
            print(el, text[k])
            text[k] = str(el).replace("/", "\/").replace("'", "\"") +",\n"

print(text)
f = open("output.json", "w", encoding="UTF-8")
cont = ""
for line in text:
    print(line)
    cont+=line
print(cont)
f.write(cont)
f.close()            
    