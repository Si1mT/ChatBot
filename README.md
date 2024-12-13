# ChatBot

The project involves training several chatbots (and QA bots) using different datasets.


<h2>Datasets used</h2>

<h4>Kaggle dataset</h4>
<p>dataset.txt (https://www.kaggle.com/datasets/grafstor/simple-dialogs-for-chatbot). The dataset has questions or prompts in the first column and answers in the second column. After we tried out various algorithms to make the model for the bot we generated data using another chatbot to see if it improves the quality of our own bot.</p>

<h4>ChatGPT-generated dataset dataset</h4>
<p>generated_dataset_clean.txt . This dataset was generated via ChatGPT4o mini. It is the combined result of various prompts, in order to avoid the problem of ChatGPT losing context mid-answer and lowering the quality of the data. The dataset has questions or prompts in the first column and answers in the second column.</p>

<h4>SQuAD dataset</h4>
<p>SQuAD dataset (https://huggingface.co/datasets/rajpurkar/squad). This is a large human-generated dataset that has contexts, questions and answers from various Wikipedia articles. In our project, we used smaller subsets of this dataset for training due to computational limitations.</p>
<br><br>

<h2>Overview of files</h2>

<h4>BoW_basic_chatbot_Kaggle-ChatGPT.ipynb</h4>
<p>This notebook contains code for training basic chatbots from scratch on the Kaggle and ChatGPT datasets. The model is based on a Bag-of-words approach and does not yield good results (which is to be expected with such an unsophisticated model).</p>

<h4>BoW_basic_QA_trained_on_SQuAD.ipynb</h4>
<p>This notebook contains code for training a basic QA bot from scratch on the SQuAD dataset. This model is also based on a Bag-of-words approach and does not yield good results.</p>

<h4>Word2Vec_SQuAD.ipynb</h4>
<p>This notebook contains code for training a basic QA bot from scratch on the SQuAD dataset. This model is Word2Vec-based, which is a significantly more sopthisticated approach than BoW, and the results also show an improvement compared to the BoW-based QA bot. That being said, the quality is still not very good and requires the questions to be worded very closely to the questions in the training data.</p>

<h4>DistilBERT_chatbot_Kaggle_ChatGPT.ipynb</h4>
<p>This notebook contains code for fine-tuning DistilBERT into chatbots, using the Kaggle and the ChatGPT-generated datasets. The results of the fine-tuning are significantly better than the basic approaches described before. When the topic of the prompts is similar enough to the training data, the bot usually stays on topic. The ChatGPT dataset seems to yield slightly better results. To improve results on the Kaggle dataset, duplicate values in the dataset were removed in order to balance the dataset. This helps avoid the bot defaulting to the most common answer every time.</p>

<h4>DistilBERT_QA_fine-tuned_SQuAD.ipynb</h4>
<p>This notebook contains code for fine-tuning DistilBERT for QA purposes, using the SQuAD dataset. The code includes training with different amounts of data. The EM and F1 scores are calculated also.</p>

<p>The code for the attempt at fine-tuning ChatGPT is located in this Google Colab notebook (to be updated): https://colab.research.google.com/drive/1oG8UQzQlpyTx3lXEYzOFiSImOLyLeCmC?usp=sharing </p>
