from zhihu import Answer

answer = Answer(url="https://www.zhihu.com/question/30913458/answer/193839736")
images = answer.images()
print(images)