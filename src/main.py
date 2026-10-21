from textnode import TextNode, TextType


def main():
    anchor = "random anchor text"
    link = "https://www.boot.dev"
    text_type = TextType.URL_LINK
    test = TextNode(anchor, text_type, link)
    print(test)

if __name__ == "__main__":
    main()
