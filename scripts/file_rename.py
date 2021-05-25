import os 

def main(): 
	for filename in os.listdir("/Users/capgemini/Downloads/pilotflyingj"):
			date=(filename.partition('customers_')[2].replace('.csv',''))
			dst1="new_af14e333cf96083199cb680435c367f5cebfe96f_"
			dst2="_auto-user_user.csv"
			new_file_name=dst1+date+dst2
			os.chdir("/Users/capgemini/Downloads/pilotflyingj")
			os.rename(filename,new_file_name) 

if __name__ == '__main__':
	main()

