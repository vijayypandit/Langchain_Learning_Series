
from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """ Space is the boundless three-dimensional extent in which objects and events have relative position and direction. In classical physics, physical space is often conceived in three linear dimensions, although modern physicists usually consider it, with time, to be part of a boundless four-dimensional continuum known as spacetime. The concept of space is considered to be of fundamental importance to an understanding of the physical universe. However, disagreement continues between philosophers over whether it is itself an entity, a relationship between entities, or part of a conceptual framework."""

#Initialize the RecursiveCharacterTextSplitter with a chunk size of 300 characters and no overlap  
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=0
)
chunks = text_splitter.split_text(text)
print(chunks)
print(len(chunks))