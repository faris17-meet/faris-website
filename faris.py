def isPalindrome(sentence):
	sentence = sentence.lower().replace("","")
	if len(sentence)==1:
		print("Palindrome!")
		return
	firtletter = sentence[0]
	lastletter = sentence[-1]
	if firstletter == lastletter:
		if len(sentence) == 2:
			print("palindrome!")
			return
		isPalindrome(sentence[1:-1])
	else:
		print("Not a palindrome!")


isAPalindrome("Abba")
isAPalindrome("I Have a puppy ")
isAPalindrome("A man, a plan, a cat, a ham, a yak, a yam, a hat, a canal-Panama!")