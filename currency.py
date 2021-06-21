 def claim():
            if earnings[len(winnings1)] >=2 or earnings[len(winnings2)] >=2 or earnings[len(winnings3)] >= 2:
                bank_details()
                text_file = open("PlayerID.txt", '+a')
                text_file.write(
                    "\nEntry 1 winning numbers : " + str() + "\nEntry 2 winning numbers : " + str(entry2) + "\nEntry 3 winning numbers : " + str(entry3))
                text_file.close()
            else:
             messagebox.showerror("Error", "You do not have any winnings to claim")
