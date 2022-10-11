import os
import re

data = list()
scripts = list()
titles = list()
README_md_path = os.path.dirname(os.path.realpath(__file__)) + os.sep + 'README.md'
print(os.getcwd())
for dirname, _, filenames in os.walk(os.path.dirname(os.path.realpath(__file__))):
    for filename in filenames:
        if filename.endswith('.py') and filename != os.path.basename(__file__):
            scripts.append(os.path.join(dirname, filename))

if os.path.exists(README_md_path):
    os.remove(README_md_path)

for script in scripts:
    f = open(script)
    line = f.readline()
    print(line)
    data = re.findall(r'# title\s*([^\s]*\n)', line)[0]
    print(data)
    titles.append(data[:-1])
    f.close()

for i in range(len(titles)):
    title = titles[i]
    titles[i] = f'+ [{title}](#{title})\n\n'
    print(titles)
titles = ''.join(titles)

f = open(README_md_path, 'a+')
f.write(titles)
f.close

for script in scripts:
    f = open(script)
    lines = f.readlines()

    for i in range(len(lines) - 1):
        line = lines[i]
        if line.startswith('# title'):
            data = re.findall(r'(#) title\s*([^\s]*\n)', line)[0]
            lines[i] = ' '.join([str(x) for x in data])
        elif line.startswith('# description'):
            lines[i] = ' '.join([str(x) for x in re.findall(r'(#) description\s*([^\s]*\n)', line)[0]])
        elif line.startswith('# code'):
            lines[i] = '```python\n'
    lines.append('\n```\n')
    f = open(README_md_path, 'a+')
    f.write(''.join(lines))
    f.close()