import opc, time

client = opc.Client('localhost:7890')
bits = ( (0,255,0), (0,255,0) )

while True:
	for strip2 in range(8):
		pixels2 = [ (90,0,90) ] * 512
		for j in range(32):
			pixels2[strip2 * 64 + j * 2] = (200,200,200)

		client.put_pixels(pixels2)
		time.sleep(0.5)

	for strip in range(8):
		pixels1 = [ (90,0,90) ] * 512
		for i in range(32):
			pixels1[strip * (-64) - i * 2] = (200,200,200)

		client.put_pixels(pixels1)
		time.sleep(0.5)

