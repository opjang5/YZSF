# coding=utf-8
import sys
import importlib
importlib.reload(sys)
from flask import Flask, request
from flask_restful import Resource, Api
#flask_restful
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
import gensim
app = Flask(__name__)
api = Api(app)
todos = {}
print("加载数据......")
print("Loading......") 
import os
model_path=os.path.abspath('.')+'/data/wiki.zh.text_bigger.vector'
model=gensim.models.KeyedVectors.load_word2vec_format(model_path, binary=False)
print("Successfully Loaded")
class gensim_word:
    def __init__(self,word,sim):
        self.word=word
        self.sim=sim
    def __repr__(self):
        return repr((self.word, self.sim))
class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        print(todo_id)
        if todo_id=='todo2':
            todos[todo_id] = request.form['data']
            word=model.most_similar(todos[todo_id])
            j=0;
            ans=['\0' for x in range(0,15)]
            for i in word:
                ans[j]=str(i)+'\n'
                j=j+1;
            return {todo_id:todos[todo_id],'0':ans[0],'1':ans[1],'2':ans[2],'3':ans[3],'4':ans[4],'5':ans[5],'6':ans[6],'7':ans[7],'8':ans[8],'9':ans[9]}
        elif todo_id=='todo1':
            todos[todo_id] = request.form['data']
            word=todos[todo_id];
            ans=['\0' for x in range(0,15)]
            ans[0]='妇科'
            ans[1]='儿科'
            ans[2]='神经内科'
            ans[3]='眼科'
            ans[4]='骨科'
            ans[5]='皮肤科'
            ans[6]='泌尿科'
            ans[7]='肾脏科'
            ans[8]='耳鼻喉科'
            ans[9]='急诊部'
            word_objects=[
                gensim_word(ans[0],model.similarity(word,ans[0])),
                gensim_word(ans[1],model.similarity(word,ans[1])),
                gensim_word(ans[2],model.similarity(word,ans[2])),
                gensim_word(ans[3],model.similarity(word,ans[3])),
                gensim_word(ans[4],model.similarity(word,ans[4])),
                gensim_word(ans[5],model.similarity(word,ans[5])),
                gensim_word(ans[6],model.similarity(word,ans[6])),
                gensim_word(ans[7],model.similarity(word,ans[7])),
                gensim_word(ans[8],model.similarity(word,ans[8])),
                gensim_word(ans[9],model.similarity(word,ans[9])),
                ]
            ans2=sorted(word_objects, key=lambda gensim_word: gensim_word.sim,reverse=True)
            for i in ans2:
                print(i)
            return {todo_id:todos[todo_id],'0':ans2[0].word+str(ans2[0].sim)+'\n','1':ans2[1].word+str(ans2[1].sim)+'\n',
                    '2':ans2[2].word+str(ans2[2].sim)+'\n','3':ans2[3].word+str(ans2[3].sim)+'\n',
                    '4':ans2[4].word+str(ans2[4].sim)+'\n','5':ans2[5].word+str(ans2[5].sim)+'\n',
                    '6':ans2[6].word+str(ans2[6].sim)+'\n','7':ans2[7].word+str(ans2[7].sim)+'\n',
                    '8':ans2[8].word+str(ans2[8].sim)+'\n','9':ans2[9].word+str(ans2[9].sim)+'\n'}

api.add_resource(TodoSimple, '/<string:todo_id>')

if __name__ == '__main__':
    while(True):
        try:
            app.run('localhost',port=5050)
        except:
            print('process exception')
def init_API1(port1):
    try:
        app.run('localhost',port=port1)
    except:
        print('process exception')
