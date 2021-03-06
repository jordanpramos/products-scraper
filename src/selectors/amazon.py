AMAZON_ROBOT_MESSAGE = "Sorry, we just need to make sure you're not a robot."

AMAZON_YML_STRING = """
    products:
        css: 'div[data-component-type="s-search-result"]'
        xpath: null
        multiple: true
        type: Text
        children:
            title:
                css: 'h2 a.a-link-normal.a-text-normal'
                xpath: null
                type: Text
            product_url:
                css: 'h2 a.a-link-normal.a-text-normal'
                xpath: null
                type: Link
            image_url:
                css: 'img'
                xpath: null
                type: Attribute
                attribute: srcset
                format: AmazonImage
            rating:
                css: 'div.a-row.a-size-small span:nth-of-type(1)'
                xpath: null
                type: Attribute
                attribute: aria-label
            reviews:
                css: 'div.a-row.a-size-small span:nth-of-type(2)'
                xpath: null
                type: Attribute
                attribute: aria-label
            price:
                css: 'span.a-price:nth-of-type(1) span.a-offscreen'
                xpath: null
                type: Text
    """