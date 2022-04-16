from skweak import heuristics, gazetteers, generative, utils
def entities(doc: doc, layer=None, add_tooltip=True):
    """Display the entities annotated in a spacy document, based on the
    provided annotation layer(s). If layer is None, the method displays
    the entities from Spacy. 
    This method will only work in a Jupyter Notebook or similar. 
    """
    import spacy.displacy
    import IPython.core.display
    if layer is None:
        spans = doc.ents
    elif type(layer) is list:
        spans = get_spans(doc, layer)
    elif type(layer) == str:
        if "*" in layer:
            matched_layers = [l for l in doc.spans
                              if re.match(layer.replace("*", ".*?")+"$", l)]
            spans = get_spans(doc, matched_layers)
        else:
            spans = doc.spans[layer]
    else:
        raise RuntimeError("Layer type not accepted")

    entities = {}
    for span in spans:

        start_char = doc[span.start].i
        end_char = doc[span.end].i

        if (start_char, end_char) not in entities:
            entities[(start_char, end_char)] = span.label_

        # If we have several alternative labels for a span, join them with +
        elif span.label_ not in entities[(start_char, end_char)]:
            entities[(start_char, end_char)] = entities[(
                start_char, end_char)] + "+" + span.label_

    entities = [{"start": start, "end": end, "label": label}
                for (start, end), label in entities.items()]
    return(entities)
