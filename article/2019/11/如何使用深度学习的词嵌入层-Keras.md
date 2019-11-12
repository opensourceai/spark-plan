原文： https://machinelearningmastery.com/use-word-embedding-layers-deep-learning-keras/ 

作者： Jason Brownlee 

翻译：[Quan Chen](https://github.com/chenquan)



# 如何使用深度学习的词嵌入层 - Keras

[单词嵌入](https://machinelearningmastery.com/what-are-word-embeddings/)提供单词及其相对含义的密集表示。

它们是对较简单的单词模型表示形式中使用的稀疏表示形式的改进。

可以从文本数据中学习单词嵌入，并在项目之间重复使用。也可以将它们作为在文本数据上安装神经网络的一部分来学习。

在本教程中，您将发现如何在Keras的Python中使用词嵌入进行深度学习。

完成本教程后，您将知道：

- 关于单词嵌入以及Keras通过Embedding层支持单词嵌入。
- 如何在拟合神经网络的同时学习单词嵌入。
- 如何在神经网络中使用预先训练的单词嵌入。

[在我的新书中](https://machinelearningmastery.com/deep-learning-for-nlp/)，通过30步循序渐进的教程和完整的源代码，探索如何开发用于文本分类，翻译，图片标题等的深度学习模型。

让我们开始吧。

- **2018年2月更新**：修复了由于基础API的更改而导致的错误。
- **2019年10月更新**：针对Keras 2.3和TensorFlow 2.0更新。



## 教程概述

本教程分为3个部分。他们是：

1. 词嵌入
2. Keras嵌入层
3. 学习嵌入的示例
4. 使用预训练的GloVe嵌入的示例



## 1.词嵌入

词嵌入是使用密集向量表示法表示词和文档的一类方法。

它是对传统的词袋模型编码方案的改进，在传统的词袋模型编码方案中，大型稀疏矢量用于表示每个单词或对矢量中的每个单词评分以表示整个词汇。这些表述是稀疏的，因为词汇量很大，并且给定的单词或文档将由一个主要由零值组成的大向量表示。

取而代之的是，在嵌入中，单词由密集的矢量表示，其中矢量表示单词在连续矢量空间中的投影。

单词在向量空间中的位置是从文本中获悉的，并且基于使用时围绕单词的单词。

单词在学习向量空间中的位置称为其嵌入。

从文本中学习单词嵌入的方法的两个流行示例包括：

- Word2Vec。
- 手套。

除了这些精心设计的方法外，单词嵌入还可以作为深度学习模型的一部分来学习。这可能是一种较慢的方法，但是可以将模型定制为特定的训练数据集。

## 2. Keras嵌入层

Keras提供了一个[嵌入](https://keras.io/layers/embeddings/#embedding)层，可用于文本数据的神经网络。

它要求输入数据是整数编码的，以便每个单词都由唯一的整数表示。可以使用[Keras](https://keras.io/preprocessing/text/#tokenizer)随附的[Tokenizer API](https://keras.io/preprocessing/text/#tokenizer)来执行此数据准备步骤。

嵌入层将使用随机权重进行初始化，并将学习训练数据集中所有单词的嵌入。

它是一个灵活的层，可以以多种方式使用，例如：

- 可以单独使用它来学习单词嵌入，该单词嵌入可以在以后的其他模型中保存和使用。
- 它可以用作深度学习模型的一部分，在该模型中，可以与模型一起学习嵌入。
- 它可以用于加载预训练的单词嵌入模型，这是一种转移学习。

嵌入层被定义为网络的第一隐藏层。它必须指定3个参数：

它必须指定3个参数：

- **input_dim**：这是文本数据中词汇的大小。例如，如果您的数据是整数编码为0-10之间的值，则词汇表的大小将为11个单词。
- **output_dim**：这是将在其中嵌入单词的向量空间的大小。它为每个单词定义了该层输出矢量的大小。例如，它可以是32或100甚至更大。为您的问题测试不同的值。
- **input_length**：这是输入序列的长度，就像您为Keras模型的任何输入层定义的那样。例如，如果您所有的输入文档都由1000个单词组成，则该值为1000。

例如，下面我们定义一个具有200个词汇量的嵌入层（例如，从0到199，包括0到199的整数编码的单词），一个将嵌入单词的32维向量空间以及每个包含50个单词的输入文档。

```python
e = Embedding(200, 32, input_length=50)
```

嵌入层具有可以学习的权重。如果将模型保存到文件，则将包括“嵌入”层的权重。

*嵌入*层的输出是2D向量，其中每个单词在输入单词序列（输入文档）中嵌入一个。

如果希望连接*密集*直接层到嵌入层，必须首先压扁2D输出矩阵使用一个一维矢量*平铺*层。

现在，让我们看看如何在实践中使用嵌入层。

## 3.学习嵌入的示例

在本节中，我们将研究如何在将神经网络拟合到[文本分类](https://machinelearningmastery.com/best-practices-document-classification-deep-learning/)问题的同时学习单词嵌入。

我们将定义一个小问题，我们有10个文本文档，每个文本文档中都有关于学生提交的一件作品的评论。每个文本文档被分类为正“ 1”或负“ 0”。这是一个简单的情感分析问题。

首先，我们将定义文档及其类标签。

```python
# define documents
docs = ['Well done!',
		'Good work',
		'Great effort',
		'nice work',
		'Excellent!',
		'Weak',
		'Poor effort!',
		'not good',
		'poor work',
		'Could have done better.']
# define class labels
labels = array([1,1,1,1,1,0,0,0,0,0])
```

接下来，我们可以对每个文档进行整数编码。这意味着作为输入，嵌入层将具有整数序列。我们可以尝试使用其他更复杂的单词模型编码包，例如count或TF-IDF。

[Keras](https://keras.io/preprocessing/text/#one_hot)提供了[one_hot（）函数](https://keras.io/preprocessing/text/#one_hot)，该[函数](https://keras.io/preprocessing/text/#one_hot)创建每个单词的哈希作为有效的整数编码。我们将估计词汇量为50，这比减少散列函数发生碰撞的可能性所需的词汇量要大得多。

```python
# integer encode the documents
vocab_size = 50
encoded_docs = [one_hot(d, vocab_size) for d in docs]
print(encoded_docs)
```

 序列具有不同的长度，Keras希望将输入向量化，并且所有输入都具有相同的长度。我们将填充所有输入序列的长度为4。再次，我们可以使用内置的[Keras](https://keras.io/preprocessing/sequence/#pad_sequences)函数（在本例中为[pad_sequences（）函数）](https://keras.io/preprocessing/sequence/#pad_sequences)来做到这一点。 

```python
# pad documents to a max length of 4 words
max_length = 4
padded_docs = pad_sequences(encoded_docs, maxlen=max_length, padding='post')
print(padded_docs)
```

现在，我们准备将*嵌入*层定义为神经网络模型的一部分。

该*嵌入*具有50词汇和为4的输入长度我们将选择8种尺寸的小嵌入空间。

该模型是简单的二进制分类模型。重要的是，*嵌入*层的输出将是4个矢量，每个矢量8个维度，每个单词一个。我们将其展平为一个包含32个元素的矢量，然后传递给*Dense*输出层。

```python
# define the model
model = Sequential()
model.add(Embedding(vocab_size, 8, input_length=max_length))
model.add(Flatten())
model.add(Dense(1, activation='sigmoid'))
# compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
# summarize the model
print(model.summary())
```

 最后，我们可以拟合和评估分类模型。 

```python
# fit the model
model.fit(padded_docs, labels, epochs=50, verbose=0)
# evaluate the model
loss, accuracy = model.evaluate(padded_docs, labels, verbose=0)
print('Accuracy: %f' % (accuracy*100))

```
下面提供了完整的代码清单。

```python
from numpy import array
from keras.preprocessing.text import one_hot
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers.embeddings import Embedding
# define documents
docs = ['Well done!',
		'Good work',
		'Great effort',
		'nice work',
		'Excellent!',
		'Weak',
		'Poor effort!',
		'not good',
		'poor work',
		'Could have done better.']
# define class labels
labels = array([1,1,1,1,1,0,0,0,0,0])
# integer encode the documents
vocab_size = 50
encoded_docs = [one_hot(d, vocab_size) for d in docs]
print(encoded_docs)
# pad documents to a max length of 4 words
max_length = 4
padded_docs = pad_sequences(encoded_docs, maxlen=max_length, padding='post')
print(padded_docs)
# define the model
model = Sequential()
model.add(Embedding(vocab_size, 8, input_length=max_length))
model.add(Flatten())
model.add(Dense(1, activation='sigmoid'))
# compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
# summarize the model
print(model.summary())
# fit the model
model.fit(padded_docs, labels, epochs=50, verbose=0)
# evaluate the model
loss, accuracy = model.evaluate(padded_docs, labels, verbose=0)
print('Accuracy: %f' % (accuracy*100))
```

 首先运行示例将打印整数编码的文档。 

```shell
[[6, 16], [42, 24], [2, 17], [42, 24], [18], [17], [22, 17], [27, 42], [22, 24], [49, 46, 16, 34]]
```

然后打印每个文档的填充版本，使它们的长度一致。

```shell
[[ 6 16  0  0]
 [42 24  0  0]
 [ 2 17  0  0]
 [42 24  0  0]
 [18  0  0  0]
 [17  0  0  0]
 [22 17  0  0]
 [27 42  0  0]
 [22 24  0  0]
 [49 46 16 34]]
```



 定义网络后，将打印各层的摘要。我们可以看到，正如预期的那样，Embedding层的输出是4×8矩阵，并且被Flatten层压缩为32个元素的向量。 

```shell
_________________________________________________________________
Layer (type)                 Output Shape              Param #
=================================================================
embedding_1 (Embedding)      (None, 4, 8)              400
_________________________________________________________________
flatten_1 (Flatten)          (None, 32)                0
_________________________________________________________________
dense_1 (Dense)              (None, 1)                 33
=================================================================
Total params: 433
Trainable params: 433
Non-trainable params: 0
_________________________________________________________________
```

 最后，打印出训练模型的准确性，表明它完美地学习了训练数据集（这不足为奇）。 

```python
Accuracy: 100.000000
```



您可以将学习的权重从“嵌入”层保存到文件中，以备将来在其他模型中使用。

您也可以通常使用此模型对测试数据集中具有相同种类词汇的其他文档进行分类。

接下来，让我们看一下如何在Keras中嵌入预训练的单词。

## 4.使用预训练的GloVe嵌入的示例

Keras嵌入层还可以使用在其他地方学到的单词嵌入。

在自然语言处理领域，学习，保存和免费使用词嵌入是很常见的。



例如，GloVe方法背后的研究人员在其网站上提供了一组经过预训练的词嵌入，这些词嵌入是根据公共领域的许可发布的。看到：

- [GloVe：单词表示的全局向量](https://nlp.stanford.edu/projects/glove/)

最小的嵌入包为822Mb，称为“ *glove.6B.zip* ”。它在10亿个令牌（单词）的数据集上训练，词汇量为40万个单词。嵌入矢量有几种不同的大小，包括50、100、200和300个尺寸。

您可以下载该嵌入集合，然后可以使用训练数据集中单词的预训练嵌入权重为Keras *嵌入*层播种。

该示例的灵感来自[Keras](https://github.com/fchollet/keras/blob/master/examples/pretrained_word_embeddings.py)项目中的一个示例：[pretrained_word_embeddings.py](https://github.com/fchollet/keras/blob/master/examples/pretrained_word_embeddings.py)。

下载并解压缩后，您将看到一些文件，其中一个是“ *Gloves.6B.100d.txt* ”，其中包含嵌入的100维版本。

如果您查看文件内部，则将在每行上看到一个标记（单词），然后是权重（100个数字）。例如，下面是嵌入ASCII文本文件的第一行示出了" *the* “的嵌入。

```
the -0.038194 -0.24487 0.72812 -0.39961 0.083172 0.043953 -0.39141 0.3344 -0.57545 0.087459 0.28787 -0.06731 0.30906 -0.26384 -0.13231 -0.20757 0.33395 -0.33848 -0.31743 -0.48336 0.1464 -0.37304 0.34577 0.052041 0.44946 -0.46971 0.02628 -0.54155 -0.15518 -0.14107 -0.039722 0.28277 0.14393 0.23464 -0.31021 0.086173 0.20397 0.52624 0.17164 -0.082378 -0.71787 -0.41531 0.20335 -0.12763 0.41367 0.55187 0.57908 -0.33477 -0.36559 -0.54857 -0.062892 0.26584 0.30205 0.99775 -0.80481 -3.0243 0.01254 -0.36942 2.2167 0.72201 -0.24978 0.92136 0.034514 0.46745 1.1079 -0.19358 -0.074575 0.23353 -0.052062 -0.22044 0.057162 -0.15806 -0.30798 -0.41625 0.37972 0.15006 -0.53212 -0.2055 -1.2526 0.071624 0.70565 0.49744 -0.42063 0.26148 -1.538 -0.30223 -0.073438 -0.28312 0.37104 -0.25217 0.016215 -0.017099 -0.38984 0.87424 -0.72569 -0.51058 -0.52028 -0.1459 0.8278 0.27062
```

如上一节所述，第一步是定义示例，将其编码为整数，然后将序列填充为相同长度。

在这种情况下，我们需要能够将单词映射到整数以及将整数映射到单词。

Keras提供了可以适合训练数据的[Tokenizer](https://keras.io/preprocessing/text/#tokenizer)类，可以通过调用*Tokenizer*类上的*texts_to_sequences（）*方法将文本一致地转换为序列，并提供对*word_index*属性中单词到整数的字典映射的访问。

```python
# define documents
docs = ['Well done!',
		'Good work',
		'Great effort',
		'nice work',
		'Excellent!',
		'Weak',
		'Poor effort!',
		'not good',
		'poor work',
		'Could have done better.']
# define class labels
labels = array([1,1,1,1,1,0,0,0,0,0])
# prepare tokenizer
t = Tokenizer()
t.fit_on_texts(docs)
vocab_size = len(t.word_index) + 1
# integer encode the documents
encoded_docs = t.texts_to_sequences(docs)
print(encoded_docs)
# pad documents to a max length of 4 words
max_length = 4
padded_docs = pad_sequences(encoded_docs, maxlen=max_length, padding='post')
print(padded_docs)
```

 接下来，我们需要将整个GloVe单词嵌入文件加载到内存中，作为单词字典到嵌入数组 

```python
# load the whole embedding into memory
embeddings_index = dict()
f = open('glove.6B.100d.txt')
for line in f:
	values = line.split()
	word = values[0]
	coefs = asarray(values[1:], dtype='float32')
	embeddings_index[word] = coefs
f.close()
print('Loaded %s word vectors.' % len(embeddings_index))
```

这很慢。过滤掉训练数据中唯一词的嵌入可能会更好。

接下来，我们需要为训练数据集中的每个单词创建一个嵌入一个矩阵。我们可以通过枚举*Tokenizer.word_index*中的所有唯一单词并从已加载的GloVe嵌入中找到嵌入权重向量来做到这一点。

结果是仅针对我们在训练期间将看到的单词的权重矩阵。

```python
# create a weight matrix for words in training docs
embedding_matrix = zeros((vocab_size, 100))
for word, i in t.word_index.items():
	embedding_vector = embeddings_index.get(word)
	if embedding_vector is not None:
		embedding_matrix[i] = embedding_vector
```



现在，我们可以像以前一样定义，拟合和评估模型。

关键区别在于，可以使用GloVe单词嵌入权重为嵌入层设置种子。我们选择了100维版本，因此必须在*output_dim*设置为100的情况下定义嵌入层。最后，我们不想在此模型中更新学习的单词权重，因此我们将模型的*可训练*属性设置为*False*。

```python
e = Embedding(vocab_size, 100, weights=[embedding_matrix], input_length=4, trainable=False)
```

 下面列出了完整的工作示例 

```python
from numpy import array
from numpy import asarray
from numpy import zeros
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers import Embedding
# define documents
docs = ['Well done!',
		'Good work',
		'Great effort',
		'nice work',
		'Excellent!',
		'Weak',
		'Poor effort!',
		'not good',
		'poor work',
		'Could have done better.']
# define class labels
labels = array([1,1,1,1,1,0,0,0,0,0])
# prepare tokenizer
t = Tokenizer()
t.fit_on_texts(docs)
vocab_size = len(t.word_index) + 1
# integer encode the documents
encoded_docs = t.texts_to_sequences(docs)
print(encoded_docs)
# pad documents to a max length of 4 words
max_length = 4
padded_docs = pad_sequences(encoded_docs, maxlen=max_length, padding='post')
print(padded_docs)
# load the whole embedding into memory
embeddings_index = dict()
f = open('../glove_data/glove.6B/glove.6B.100d.txt')
for line in f:
	values = line.split()
	word = values[0]
	coefs = asarray(values[1:], dtype='float32')
	embeddings_index[word] = coefs
f.close()
print('Loaded %s word vectors.' % len(embeddings_index))
# create a weight matrix for words in training docs
embedding_matrix = zeros((vocab_size, 100))
for word, i in t.word_index.items():
	embedding_vector = embeddings_index.get(word)
	if embedding_vector is not None:
		embedding_matrix[i] = embedding_vector
# define model
model = Sequential()
e = Embedding(vocab_size, 100, weights=[embedding_matrix], input_length=4, trainable=False)
model.add(e)
model.add(Flatten())
model.add(Dense(1, activation='sigmoid'))
# compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
# summarize the model
print(model.summary())
# fit the model
model.fit(padded_docs, labels, epochs=50, verbose=0)
# evaluate the model
loss, accuracy = model.evaluate(padded_docs, labels, verbose=0)
print('Accuracy: %f' % (accuracy*100))
```

 运行该示例可能会花费更长的时间，但是随后证明了它能够解决这个简单的问题。 

```
[[6, 2], [3, 1], [7, 4], [8, 1], [9], [10], [5, 4], [11, 3], [5, 1], [12, 13, 2, 14]]

[[ 6  2  0  0]
 [ 3  1  0  0]
 [ 7  4  0  0]
 [ 8  1  0  0]
 [ 9  0  0  0]
 [10  0  0  0]
 [ 5  4  0  0]
 [11  3  0  0]
 [ 5  1  0  0]
 [12 13  2 14]]

Loaded 400000 word vectors.

_________________________________________________________________
Layer (type)                 Output Shape              Param #
=================================================================
embedding_1 (Embedding)      (None, 4, 100)            1500
_________________________________________________________________
flatten_1 (Flatten)          (None, 400)               0
_________________________________________________________________
dense_1 (Dense)              (None, 1)                 401
=================================================================
Total params: 1,901
Trainable params: 401
Non-trainable params: 1,500
_________________________________________________________________


Accuracy: 100.000000
```

 在实践中，我鼓励您尝试使用固定的预训练嵌入来学习单词嵌入，并尝试在预训练嵌入的基础上进行学习。 