#!/user/bin/python

import json
import lession_json
import lession_oracle

if __name__ == '__main__':
    foot={}
    name=['appple','dog','bananer']
    number=[1,2,3]
    for index in range(len(name)):
        foot[number[index]]=name[index]
        
    js=json.dumps(foot)
    print(foot)
    print(js)
    
    foot=dict(zip(name,number))
    print(foot)