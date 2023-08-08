
def dot_product(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Vectors must have the same length")
    
    dot_result = 0
    for i in range(len(v1)):
        dot_result += v1[i] * v2[i]
    
    return dot_result

def are_orthogonal(v1, v2):
    dot_result = dot_product(v1, v2)
    return dot_result == 0


def main():
    n = int(input("Enter the number of vector pairs: "))
    
    for _ in range(n):
        v1_str = input("Enter the first vector separated by spaces: ")
        v2_str = input("Enter the second vector separated by spaces: ")
        
        v1 = list(map(float, v1_str.split()))
        v2 = list(map(float, v2_str.split()))
        
        if are_orthogonal(v1, v2):
            print("The two vectors are orthogonal.")
        else:
            print("The two vectors are not orthogonal.")

if __name__ == "__main__":
    main()
