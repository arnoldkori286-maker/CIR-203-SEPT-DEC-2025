routes = ["North Road", "East Lane", "South Express", "New Street", "West Highway",
          "Northern Gate", "City Route", "Main Avenue", "New Bridge", "Express Line"]
print("Original routes:", routes)

routes.append("Lakeside Way")
routes.remove("New Street")
print("\nAfter update:", routes)

routes.sort()
routes.reverse()
print("\nSorted + reversed:", routes)

count_N = sum([1 for r in routes if r.startswith("N")])
print("\nRoutes starting with 'N':", count_N)

long_routes = [r for r in routes if len(r) > 10]
print("\nRoutes longer than 10 characters:", long_routes)
