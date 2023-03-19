# python3


def build_heap(data):
  swaps = []
  # TODO: Creat heap and heap sort
  # try to achieve  O(n) and not O(n2)
  for i in range(len(data) // 2, -1, -1):
    next_swap(i, data, swaps)

  return swaps


def next_swap(i, data, change_list):
  smallest_index = i
  l_index = 2 * i + 1
  r_index = 2 * i + 2
  if l_index < len(data) and data[l_index] < data[smallest_index]:
    smallest_index = l_index
  if r_index < len(data) and data[r_index] < data[smallest_index]:
    smallest_index = r_index

  if i != smallest_index:
    data[i], data[smallest_index] = data[smallest_index], data[i]
    change_list.append((i, smallest_index))
    next_swap(smallest_index, data, change_list)


def main():
  inp = input()

  if inp == "i":
    n = int(input().strip())
    data = list(map(int, input().strip().split()))
  elif inp == "f":
    inp2 = input()
    try:
      with open("./tests/" + inp2, mode='r') as fails:
        n = int(fails.readline())
        nums = fails.readline().split()
        data = list(map(int, nums))
    except:
      return
  else:
    print("Something went wrong")
    return

  assert len(data) == n

  change_list = build_heap(data)
  print(len(change_list))
  for (i, j) in change_list:
    print(i, j)


if __name__ == "__main__":
  main()
