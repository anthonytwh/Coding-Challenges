#Fizzz Buzz Game 

x = 1
y = 100
fizz = 3
buzz = 5


class FizzBuzz:

	def RunGame(self, startnum, endnum, Fizz, Buzz):

		for num in range(startnum, endnum + 1):
			out = ""
			
			if (num%int('{a}'.format(a=Fizz)) == 0):
				out = out + "Fizz"

			if (num%int('{b}'.format(b =Buzz)) == 0):
				out = out + "Buzz"

			if not (out == ""):
				print (out)
			else:
				print (num)

if __name__ == "__main__":
	FizzBuzz().RunGame(x, y, fizz, buzz)