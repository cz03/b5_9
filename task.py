class StopWatch:
	def __init__(self, num_runs):
		self.num_runs = num_runs

	def __enter__(self):
		self.runner()
		
	def time_this(func):
		import time
		def wrapper(self):
			avr_time = 0
			for i in range(self.num_runs):
				t0 = time.time()
				func()
				t1 = time.time()
				avr_time += (t1 - t0)
			self.res = (avr_time / self.num_runs)
		return wrapper

	@time_this
	def runner():
		for i in range(1000000):
			pass

	def __exit__(self, *args):
		print(self)

	def __str__(self):
		return f"Исполнение занимает {self.res:.5f} секунд."


with StopWatch(10):
	pass