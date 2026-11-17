about = open('about.html', encoding='utf-8').read()
blog = open('blog.html', encoding='utf-8').read()

print('about cta section:\n', about[about.rfind('<section'):about.rfind('<div id="foot"')])
print('blog cta section:\n', blog[blog.rfind('<section'):blog.rfind('<div id="foot"')])
