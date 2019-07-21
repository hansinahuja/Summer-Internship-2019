dependencies = input("Enter order of dependencies: ")
cache_size = int(input("Enter size of cache: "))
misses = 0
cache = list()
print("Sequence of cache: ")

for i in range(len(dependencies)):

    if dependencies[i] in cache:
        print("Day", i+1, ": ", cache)
        continue

    else:
        if len(cache) < cache_size:
            cache.append(dependencies[i])

        else:
            remaining = dependencies[i+1: ]
            indicator = list()
            for item in cache:
                if item in remaining:
                    indicator.append((1, item))
                else:
                    indicator.append((0, item))

            indicator.sort()
            if indicator[0][0] == 0:
                cache.remove(indicator[0][1])
                cache.append(dependencies[i])
                misses += 1

            else:
                appearance = list()
                j=0
                while len(appearance) != len(cache):
                    if remaining[j] in cache:
                        appearance.append(remaining[j])
                    j += 1
                cache.remove(appearance[-1])
                cache.append(dependencies[i])
                misses += 1

    print("Day", i+1, ": ", cache)


print("Cache misses = ", misses)

