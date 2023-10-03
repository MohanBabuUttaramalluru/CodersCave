import time

def typing_speed_test():
    passage = "The quick brown fox jumps over the lazy dog"
    
    print("Type the following text as fast as you can:")
    print(passage)
    
    input("Press Enter to start...")
    
    start_time = time.time()
    user_input = input("Start typing: ")
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    word_count = len(passage.split())
    user_word_count = len(user_input.split())
    
    correct_words = sum(a == b for a, b in zip(passage.split(), user_input.split()))
    
    print("\nTyping Speed Test Results:")
    print(f"Elapsed Time: {elapsed_time:.2f} seconds")
    print(f"Total Words in Passage: {word_count}")
    print(f"Words Typed: {user_word_count}")
    print(f"Correct Words: {correct_words}")
    print(f"Words Per Minute (WPM): {correct_words / elapsed_time * 60:.2f}")

if __name__ == "__main__":
    typing_speed_test()
