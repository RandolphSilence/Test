from collections import Counter

urls = [
"http://www.google.com/a.txt",
"http://www.google.com.tw/a.txt",
"http://www.google.com/download/c.jpg",
"http://www.google.co.jp/a.txt",
"http://www.google.com/b.txt",
"https://facebook.com/movie/b.txt",
"http://yahoo.com/123/000/c.jpg",
"http://gliacloud.com/haha.png",
]

filenames = []

for i in range(len(urls)):
    url = urls[i]
    url_ary = url.split('/')
    filenames.append(url_ary[-1])
 
cnt = Counter()
for word in filenames:
    cnt[word] += 1

for k, v in cnt.most_common(3):
    print('%s: %i' % (k, v))
