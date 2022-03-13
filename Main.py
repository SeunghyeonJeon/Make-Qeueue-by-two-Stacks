# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

class Stack:
	def __init__(self):
		self.items =[]
		
	def push(self, val):
		self.items.append(val)
		
	def pop(self):
		try:
			return(self.items.pop())
		except IndexError:
			print("EMPTY")
			
	def top(self):
		try:
			return self.items[-1]
		except IndexError:
			print("Stack is empty")
			
	def __len__(self):
		return len(self.items)
	
	def isEmpty(self):
		return self.__len__() == 0
# 기존의 Stack 클래스 정의
	
	
S1 = Stack()
S2 = Stack()
# 2개의 스택 S1, S2를 정의한다.
	
while 1:
	var = input().split()
	
	if var[0] == 'enq':  
		S1.push(var[1])
	# Enqueue 정의, S1 stack에 push 하여 값을 저장
	# stack 의 push 를 활용함으로 O(1) 시간 동작
		
	elif var[0] == 'deq':
		if S2.isEmpty() :
			while not S1.isEmpty():
				S2.push(S1.pop())
	
		val = S2.pop()
	# Dequeue 정의, S2 stack에 S1 에 저장된 값을 옮겨 담고, 한번 pop 시킨다. 
	# 옮겨담는 시기는, 첫 dequeue가 선언되었을때와 그 다음부터는 S2가 비어있을때이다.
	# 일반적으로, S2에 옮겨진 값을 pop 함으로써 해결할 수 있으므로 O(1) 시간안에 동작할 수 있다고 본다.
	
		if(val is None) :
			continue
		else:
			print(val)
  # 출력에 대한 정의
		
	else:
		break
			
