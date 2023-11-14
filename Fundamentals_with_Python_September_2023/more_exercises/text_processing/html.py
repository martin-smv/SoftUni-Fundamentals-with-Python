# Printing the title
print(f"<h1>\n"
      f"    {input()}\n"
      f"</h1>")

# Printing the content
print(f"<article>\n"
      f"    {input()}\n"
      f"</article>")

while True:
    command = input()
    if command == "end of comments":
        break

    print(f"<div>\n"
          f"    {command}\n"
          f"</div>")