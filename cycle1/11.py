def bubble_sort(arr):
    n = len(arr)


    for i in range(n):

        swapped = False


        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True


        if not swapped:
            break


try:
    print("RIYA ROY - SJC22MCA-2045")
    print("BATCH: 2022-2024")
    elements = input("Enter elements separated by spaces: ").split()
    elements = [int(x) for x in elements]

    bubble_sort(elements)

    print("Sorted elements:")
    print(elements)
except ValueError:
    print("Invalid input. Please enter valid numbers separated by spaces.")
