#모듈의 경로

'''
1.스크립트가 들어 있는 디렉토리
2.pythonpath
3.표준라비으러리 디렉토리(ex->c:\python36\lib)
sys.path.append('추가할 경로')
sys.path.remove('제거할경로')
'''

import sys,ex
print(dir(ex.sam))
print('---------------')
print(sys.path)
