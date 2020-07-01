<img src="https://github.com/natasha/natasha-logos/blob/master/naeval.svg">

Naeval — comparing quality and performance of NLP systems for Russian language. Naeval is used to evaluate <a href="https://github.com/natasha">project Natasha</a> components: <a href="https://github.com/natasha/razdel">Razdel</a>, <a href="https://github.com/natasha/navec">Navec</a>, <a href="https://github.com/natasha/slovnet">Slovnet</a>.

## Models

<table>

<tr>
<th>Model</th>
<th>Tags</th>
<th>Description</th>
</tr>

<tr>
<td>
DeepPavlov NER
<a name="deeppavlov_ner">
<a href="#deeppavlov_ner"><code>#</code></a>
</td>
<td><code>ner</code></td>
<td>
BiLSTM-CRF NER trained on Collection5.
<a href="https://github.com/deepmipt/ner">Original epo</a>,
<a href="http://docs.deeppavlov.ai/en/master/features/models/ner.html">docs</a>,
<a href="https://arxiv.org/pdf/1709.09686.pdf">paper</a>.
</td>
</tr>

<tr>
<td>
DeepPavlov BERT NER
<a name="deeppavlov_bert_ner">
<a href="#deeppavlov_bert_ner"><code>#</code></a>
</td>
<td>
<code>ner</code>
</td>
<td>
Current SOTA for Russian language.
<a href="http://docs.deeppavlov.ai/en/master/features/models/bert.html#bert-for-named-entity-recognition-sequence-tagging">Docs</a>,
<a href="https://www.youtube.com/watch?v=eKTA8i8s-zs">video</a>.
</td>
</tr>

<tr>
<td>
<a href="https://github.com/deepmipt/Slavic-BERT-NER">DeepPavlov Slavic BERT NER</a>
<a name="deeppavlov_slavic_bert_ner">
<a href="#deeppavlov_slavic_bert_ner"><code>#</code></a>
</td>
<td>
<code>ner</code>
</td>
<td>
DeepPavlov solution for BSNLP-2019. <a href="https://www.aclweb.org/anthology/W19-3712/">Paper</a>.
</td>
</tr>

<tr>
<td>
DeepPavlov Morph
<a name="deeppavlov_morph">
<a href="#deeppavlov_morph"><code>#</code></a>
</td>
<td>
<code>morph</code>
</td>
<td>
<a href="http://docs.deeppavlov.ai/en/master/features/models/morphotagger.html">Docs</a>.
</td>
</tr>

<tr>
<td>
DeepPavlov BERT Morph
<a name="deeppavlov_bert_morph">
<a href="#deeppavlov_bert_morph"><code>#</code></a>
</td>
<td>
<code>morph</code>
</td>
<td>
<a href="http://docs.deeppavlov.ai/en/master/features/models/bert.html#bert-for-morphological-tagging">Docs</a>.
</td>
</tr>

<tr>
<td>
DeepPavlov BERT Syntax
<a name="deeppavlov_bert_syntax">
<a href="#deeppavlov_bert_syntax"><code>#</code></a>
</td>
<td>
<code>syntax</code>
</td>
<td>
BERT + biaffine head. <a href="http://docs.deeppavlov.ai/en/master/features/models/syntaxparser.html">Docs</a>.
</td>
</tr>

<tr>
<td>
<a href="https://github.com/natasha/slovnet#ner">Slovnet NER</a>
<a name="slovnet_ner">
<a href="#slovnet_ner"><code>#</code></a>
</td>
<td>
<code>ner</code>
</td>
<td>
</td>
</tr>

<tr>
<td>
Slovnet BERT NER
<a name="slovnet_bert_ner">
<a href="#slovnet_bert_ner"><code>#</code></a>
</td>
<td>
<code>ner</code>
</td>
<td>
</td>
</tr>

<tr>
<td>
<a href="https://github.com/natasha/slovnet#morph">Slovnet Morph</a>
<a name="slovnet_morph">
<a href="#slovnet_morph"><code>#</code></a>
</td>
<td>
<code>morph</code>
</td>
<td>
</td>
</tr>

<tr>
<td>
Slovnet BERT Morph
<a name="slovnet_bert_morph">
<a href="#slovnet_bert_morph"><code>#</code></a>
</td>
<td>
<code>morph</code>
</td>
<td>
</td>
</tr>

<tr>
<td>
<a href="https://github.com/natasha/slovnet#syntax">Slovnet Syntax</a>
<a name="slovnet_syntax">
<a href="#slovnet_syntax"><code>#</code></a>
</td>
<td>
<code>syntax</code>
</td>
<td>
</td>
</tr>

<tr>
<td>
Slovnet BERT Syntax
<a name="slovnet_bert_syntax">
<a href="#slovnet_bert_syntax"><code>#</code></a>
</td>
<td>
<code>syntax</code>
</td>
<td>
</td>
</tr>

<tr>
<td>
<a href="http://pullenti.ru/">PullEnti</a>
<a name="pullenti">
<a href="#pullenti"><code>#</code></a>
</td>
<td>
<code>ner</code>
<code>morph</code>
</td>
<td>
First place on factRuEval-2016, super sophisticated ruled based system.
</td>
</tr>

<tr>
<td>
<a href="https://stanfordnlp.github.io/stanza/">Stanza</a>
<a name="stanza">
<a href="#stanza"><code>#</code></a>
</td>
<td>
<code>ner</code>
<code>morph</code>
<code>syntax</code>
</td>
<td>
Tool by Stanford NLP released in 2020. <a href="https://arxiv.org/pdf/2003.07082.pdf">Paper</a>.
</td>
</tr>

<tr>
<td>
<a href="https://spacy.io/">SpaCy</a>
<a name="spacy">
<a href="#spacy"><code>#</code></a>
</td>
<td>
<code>ner</code>
<code>morph</code>
<code>syntax</code>
</td>
<td>
Uses <a href="https://github.com/buriy/spacy-ru">Russian models</a> trained by @buriy.
</td>
</tr>

<tr>
<td>
<a href="https://texterra.ispras.ru">Texterra</a>
<a name="texterra">
<a href="#texterra"><code>#</code></a>
</td>
<td>
<code>morph</code>
<code>syntax</code>
<code>ner</code>
<code>token</code>
<code>sent</code>
</td>
<td>
Multifunctional NLP solution by <a href="https://www.ispras.ru/">ISP RAS</a>.
</td>
</tr>

<tr>
<td>
<a href="https://github.com/yandex/tomita-parser/">Tomita</a>
<a name="tomita">
<a href="#tomita"><code>#</code></a>
</td>
<td>
<code>ner</code>
</td>
GLR-parser by Yandex, only implementation for person names is publicly available.
<td>
</td>
</tr>

<tr>
<td>
<a href="https://github.com/mit-nlp/MITIE">MITIE</a>
<a name="mitie">
<a href="#mitie"><code>#</code></a>
</td>
<td>
<code>ner</code>
</td>
<td>
Engine developed at MIT + <a href="http://lang.org.ua/en/models/">third party model for Russian language</a>
</td>
</tr>

<tr>
<td>
<a href="https://github.com/Koziev/rupostagger">RuPosTagger</a>
<a name="rupostagger">
<a href="#rupostagger"><code>#</code></a>
</td>
<td>
<code>morph</code>
</td>
<td>
CRF tagger, part of <a href="http://www.solarix.ru/">Solarix project</a>.
</td>
</tr>

<tr>
<td>
RNNMorph
<a name="rnnmorph">
<a href="#rnnmorph"><code>#</code></a>
</td>
<td>
<code>morph</code>
</td>
<td>
First place solution on morphoRuEval-2017. <a href="https://habr.com/ru/post/339954/">Porst on Habr</a>.
</td>
</tr>

<tr>
<td>
<a href="http://ufal.mff.cuni.cz/udpipe">UDPipe</a>
<a name="udpipe">
<a href="#udpipe"><code>#</code></a>
</td>
<td>
<code>morph</code>
<code>syntax</code>
</td>
<td>
Model trained on SynTagRus.
</td>
</tr>

<!-- <tr> -->
<!-- <td> -->
<!-- <a name=""> -->
<!-- <a href="#"><code>#</code></a> -->
<!-- </td> -->
<!-- <td> -->
<!-- <code></code> -->
<!-- </td> -->
<!-- <td> -->
<!-- </td> -->
<!-- </tr> -->


</table>

## Tokenization

See <a href="https://github.com/natasha/razdel#evaluation">Razdel evalualtion section</a> for more info.

<!--- token --->
<table border="0" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="2" halign="left">corpora</th>
      <th colspan="2" halign="left">syntag</th>
      <th colspan="2" halign="left">gicrya</th>
      <th colspan="2" halign="left">rnc</th>
    </tr>
    <tr>
      <th></th>
      <th>errors</th>
      <th>time</th>
      <th>errors</th>
      <th>time</th>
      <th>errors</th>
      <th>time</th>
      <th>errors</th>
      <th>time</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>re.findall(\w+|\d+|\p+)</th>
      <td>24</td>
      <td>0.5</td>
      <td>16</td>
      <td>0.5</td>
      <td>19</td>
      <td>0.4</td>
      <td>60</td>
      <td>0.4</td>
    </tr>
    <tr>
      <th>spacy</th>
      <td>26</td>
      <td>6.2</td>
      <td>13</td>
      <td>5.8</td>
      <td><b>14</b></td>
      <td>4.1</td>
      <td>32</td>
      <td>3.9</td>
    </tr>
    <tr>
      <th>nltk.word_tokenize</th>
      <td>60</td>
      <td>3.4</td>
      <td>256</td>
      <td>3.3</td>
      <td>75</td>
      <td>2.7</td>
      <td>199</td>
      <td>2.9</td>
    </tr>
    <tr>
      <th>mystem</th>
      <td>23</td>
      <td>5.0</td>
      <td>15</td>
      <td>4.7</td>
      <td>19</td>
      <td>3.7</td>
      <td><b>14</b></td>
      <td>3.9</td>
    </tr>
    <tr>
      <th>mosestokenizer</th>
      <td><b>11</b></td>
      <td><b>2.1</b></td>
      <td><b>8</b></td>
      <td><b>1.9</b></td>
      <td>15</td>
      <td><b>1.6</b></td>
      <td><b>16</b></td>
      <td><b>1.7</b></td>
    </tr>
    <tr>
      <th>segtok.word_tokenize</th>
      <td>16</td>
      <td><b>2.3</b></td>
      <td><b>8</b></td>
      <td><b>2.3</b></td>
      <td>14</td>
      <td><b>1.8</b></td>
      <td><b>9</b></td>
      <td><b>1.8</b></td>
    </tr>
    <tr>
      <th>aatimofeev/spacy_russian_tokenizer</th>
      <td>17</td>
      <td>48.7</td>
      <td><b>4</b></td>
      <td>51.1</td>
      <td><b>5</b></td>
      <td>39.5</td>
      <td>20</td>
      <td>52.2</td>
    </tr>
    <tr>
      <th>koziev/rutokenizer</th>
      <td><b>15</b></td>
      <td><b>1.1</b></td>
      <td>8</td>
      <td><b>1.0</b></td>
      <td>23</td>
      <td><b>0.8</b></td>
      <td>68</td>
      <td><b>0.9</b></td>
    </tr>
    <tr>
      <th>razdel.tokenize</th>
      <td><b>9</b></td>
      <td>2.9</td>
      <td>9</td>
      <td>2.8</td>
      <td><b>3</b></td>
      <td>2.0</td>
      <td>16</td>
      <td>2.2</td>
    </tr>
  </tbody>
</table>
<!--- token --->

## Sentence segmentation

<!--- sent --->
<table border="0" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="2" halign="left">corpora</th>
      <th colspan="2" halign="left">syntag</th>
      <th colspan="2" halign="left">gicrya</th>
      <th colspan="2" halign="left">rnc</th>
    </tr>
    <tr>
      <th></th>
      <th>errors</th>
      <th>time</th>
      <th>errors</th>
      <th>time</th>
      <th>errors</th>
      <th>time</th>
      <th>errors</th>
      <th>time</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>re.split([.?!…])</th>
      <td>114</td>
      <td>0.9</td>
      <td>53</td>
      <td>0.6</td>
      <td>63</td>
      <td>0.7</td>
      <td>130</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>segtok.split_single</th>
      <td>106</td>
      <td>17.8</td>
      <td><b>36</b></td>
      <td>13.4</td>
      <td>1001</td>
      <td><b>1.1</b></td>
      <td>912</td>
      <td><b>2.8</b></td>
    </tr>
    <tr>
      <th>mosestokenizer</th>
      <td>238</td>
      <td><b>8.9</b></td>
      <td>182</td>
      <td><b>5.7</b></td>
      <td>80</td>
      <td>6.4</td>
      <td>287</td>
      <td><b>7.4</b></td>
    </tr>
    <tr>
      <th>nltk.sent_tokenize</th>
      <td><b>92</b></td>
      <td><b>10.1</b></td>
      <td><b>36</b></td>
      <td><b>5.3</b></td>
      <td><b>44</b></td>
      <td><b>5.6</b></td>
      <td><b>183</b></td>
      <td>8.9</td>
    </tr>
    <tr>
      <th>deeppavlov/rusenttokenize</th>
      <td><b>57</b></td>
      <td>10.9</td>
      <td><b>10</b></td>
      <td>7.9</td>
      <td><b>56</b></td>
      <td>6.8</td>
      <td><b>119</b></td>
      <td><b>7.0</b></td>
    </tr>
    <tr>
      <th>razdel.sentenize</th>
      <td><b>52</b></td>
      <td><b>6.1</b></td>
      <td><b>7</b></td>
      <td><b>3.9</b></td>
      <td><b>72</b></td>
      <td><b>4.5</b></td>
      <td><b>59</b></td>
      <td>7.5</td>
    </tr>
  </tbody>
</table>
<!--- sent --->

## Pretrained embeddings

See <a href="https://github.com/natasha/navec#evaluation">Navec evalualtion section</a> for more info.

<!--- emb1 --->
<table border="0" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>type</th>
      <th>init, s</th>
      <th>get, µs</th>
      <th>disk, mb</th>
      <th>ram, mb</th>
      <th>vocab</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>hudlit_12B_500K_300d_100q</th>
      <td>navec</td>
      <td><b>1.0</b></td>
      <td>19.9</td>
      <td><b>50.6</b></td>
      <td><b>95.3</b></td>
      <td><b>500K</b></td>
    </tr>
    <tr>
      <th>news_1B_250K_300d_100q</th>
      <td>navec</td>
      <td><b>0.5</b></td>
      <td>20.3</td>
      <td><b>25.4</b></td>
      <td><b>47.7</b></td>
      <td><b>250K</b></td>
    </tr>
    <tr>
      <th>ruscorpora_upos_cbow_300_20_2019</th>
      <td>w2v</td>
      <td>12.1</td>
      <td><b>1.6</b></td>
      <td><b>220.6</b></td>
      <td><b>236.1</b></td>
      <td>189K</td>
    </tr>
    <tr>
      <th>ruwikiruscorpora_upos_skipgram_300_2_2019</th>
      <td>w2v</td>
      <td>15.7</td>
      <td><b>1.7</b></td>
      <td>290.0</td>
      <td>309.4</td>
      <td>248K</td>
    </tr>
    <tr>
      <th>tayga_upos_skipgram_300_2_2019</th>
      <td>w2v</td>
      <td>15.7</td>
      <td><b>1.2</b></td>
      <td>290.7</td>
      <td>310.9</td>
      <td><b>249K</b></td>
    </tr>
    <tr>
      <th>tayga_none_fasttextcbow_300_10_2019</th>
      <td>fasttext</td>
      <td>11.3</td>
      <td>14.3</td>
      <td>2741.9</td>
      <td>2746.9</td>
      <td>192K</td>
    </tr>
    <tr>
      <th>araneum_none_fasttextcbow_300_5_2018</th>
      <td>fasttext</td>
      <td><b>7.8</b></td>
      <td>15.4</td>
      <td>2752.1</td>
      <td>2754.7</td>
      <td>195K</td>
    </tr>
  </tbody>
</table>
<!--- emb1 --->

<!--- emb2 --->
<table border="0" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>type</th>
      <th>simlex</th>
      <th>hj</th>
      <th>rt</th>
      <th>ae</th>
      <th>ae2</th>
      <th>lrwc</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>hudlit_12B_500K_300d_100q</th>
      <td>navec</td>
      <td>0.310</td>
      <td><b>0.707</b></td>
      <td><b>0.842</b></td>
      <td><b>0.931</b></td>
      <td><b>0.923</b></td>
      <td><b>0.604</b></td>
    </tr>
    <tr>
      <th>news_1B_250K_300d_100q</th>
      <td>navec</td>
      <td>0.230</td>
      <td>0.590</td>
      <td>0.784</td>
      <td><b>0.866</b></td>
      <td>0.861</td>
      <td>0.589</td>
    </tr>
    <tr>
      <th>ruscorpora_upos_cbow_300_20_2019</th>
      <td>w2v</td>
      <td><b>0.359</b></td>
      <td>0.685</td>
      <td><b>0.852</b></td>
      <td>0.758</td>
      <td><b>0.896</b></td>
      <td>0.602</td>
    </tr>
    <tr>
      <th>ruwikiruscorpora_upos_skipgram_300_2_2019</th>
      <td>w2v</td>
      <td>0.321</td>
      <td><b>0.723</b></td>
      <td>0.817</td>
      <td><b>0.801</b></td>
      <td>0.860</td>
      <td><b>0.629</b></td>
    </tr>
    <tr>
      <th>tayga_upos_skipgram_300_2_2019</th>
      <td>w2v</td>
      <td><b>0.429</b></td>
      <td><b>0.749</b></td>
      <td><b>0.871</b></td>
      <td>0.771</td>
      <td><b>0.899</b></td>
      <td><b>0.639</b></td>
    </tr>
    <tr>
      <th>tayga_none_fasttextcbow_300_10_2019</th>
      <td>fasttext</td>
      <td><b>0.369</b></td>
      <td>0.639</td>
      <td>0.793</td>
      <td>0.682</td>
      <td>0.813</td>
      <td>0.536</td>
    </tr>
    <tr>
      <th>araneum_none_fasttextcbow_300_5_2018</th>
      <td>fasttext</td>
      <td>0.349</td>
      <td>0.671</td>
      <td>0.801</td>
      <td>0.706</td>
      <td>0.793</td>
      <td>0.579</td>
    </tr>
  </tbody>
</table>
<!--- emb2 --->

## Morphology taggers

See <a href="https://github.com/natasha/slovnet#morphology-1">Slovnet evaluation section</a> for more info.

<!--- morph1 --->
<table border="0" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>news</th>
      <th>wiki</th>
      <th>fiction</th>
      <th>social</th>
      <th>poetry</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>slovnet</th>
      <td><b>0.961</b></td>
      <td>0.815</td>
      <td>0.905</td>
      <td>0.807</td>
      <td>0.664</td>
    </tr>
    <tr>
      <th>slovnet_bert</th>
      <td><b>0.982</b></td>
      <td><b>0.884</b></td>
      <td><b>0.990</b></td>
      <td><b>0.890</b></td>
      <td><b>0.856</b></td>
    </tr>
    <tr>
      <th>deeppavlov</th>
      <td>0.940</td>
      <td><b>0.841</b></td>
      <td>0.944</td>
      <td>0.870</td>
      <td><b>0.857</b></td>
    </tr>
    <tr>
      <th>deeppavlov_bert</th>
      <td><b>0.951</b></td>
      <td><b>0.868</b></td>
      <td><b>0.964</b></td>
      <td><b>0.892</b></td>
      <td><b>0.865</b></td>
    </tr>
    <tr>
      <th>udpipe</th>
      <td>0.918</td>
      <td>0.811</td>
      <td><b>0.957</b></td>
      <td>0.870</td>
      <td>0.776</td>
    </tr>
    <tr>
      <th>spacy</th>
      <td>0.919</td>
      <td>0.812</td>
      <td>0.938</td>
      <td>0.836</td>
      <td>0.729</td>
    </tr>
    <tr>
      <th>stanza</th>
      <td>0.934</td>
      <td>0.840</td>
      <td>0.940</td>
      <td><b>0.873</b></td>
      <td>0.825</td>
    </tr>
    <tr>
      <th>rnnmorph</th>
      <td>0.896</td>
      <td>0.812</td>
      <td>0.890</td>
      <td>0.860</td>
      <td>0.838</td>
    </tr>
    <tr>
      <th>maru</th>
      <td>0.894</td>
      <td>0.808</td>
      <td>0.887</td>
      <td>0.861</td>
      <td>0.840</td>
    </tr>
    <tr>
      <th>rupostagger</th>
      <td>0.673</td>
      <td>0.645</td>
      <td>0.661</td>
      <td>0.641</td>
      <td>0.636</td>
    </tr>
  </tbody>
</table>
<!--- morph1 --->

<!--- morph2 --->
<table border="0" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>init, s</th>
      <th>disk, mb</th>
      <th>ram, mb</th>
      <th>speed, it/s</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>slovnet</th>
      <td><b>1.0</b></td>
      <td><b>27</b></td>
      <td><b>115</b></td>
      <td><b>532.0</b></td>
    </tr>
    <tr>
      <th>slovnet_bert</th>
      <td>5.0</td>
      <td>475</td>
      <td>8087</td>
      <td><b>285.0 (gpu)</b></td>
    </tr>
    <tr>
      <th>deeppavlov</th>
      <td><b>4.0</b></td>
      <td>32</td>
      <td>10240</td>
      <td>90.0 (gpu)</td>
    </tr>
    <tr>
      <th>deeppavlov_bert</th>
      <td>20.0</td>
      <td>1393</td>
      <td>8704</td>
      <td>85.0 (gpu)</td>
    </tr>
    <tr>
      <th>udpipe</th>
      <td>6.9</td>
      <td>45</td>
      <td><b>242</b></td>
      <td>56.2</td>
    </tr>
    <tr>
      <th>spacy</th>
      <td>8.0</td>
      <td>89</td>
      <td>579</td>
      <td>50.0</td>
    </tr>
    <tr>
      <th>stanza</th>
      <td><b>2.0</b></td>
      <td>591</td>
      <td>393</td>
      <td><b>92.0</b></td>
    </tr>
    <tr>
      <th>rnnmorph</th>
      <td>8.7</td>
      <td><b>10</b></td>
      <td>289</td>
      <td>16.6</td>
    </tr>
    <tr>
      <th>maru</th>
      <td>15.8</td>
      <td>44</td>
      <td>370</td>
      <td>36.4</td>
    </tr>
    <tr>
      <th>rupostagger</th>
      <td>4.8</td>
      <td><b>3</b></td>
      <td><b>118</b></td>
      <td>48.0</td>
    </tr>
  </tbody>
</table>
<!--- morph2 --->

## Syntax parser

<!--- syntax1 --->
<table border="0" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="2" halign="left">news</th>
      <th colspan="2" halign="left">wiki</th>
      <th colspan="2" halign="left">fiction</th>
      <th colspan="2" halign="left">social</th>
      <th colspan="2" halign="left">poetry</th>
    </tr>
    <tr>
      <th></th>
      <th>uas</th>
      <th>las</th>
      <th>uas</th>
      <th>las</th>
      <th>uas</th>
      <th>las</th>
      <th>uas</th>
      <th>las</th>
      <th>uas</th>
      <th>las</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>slovnet</th>
      <td>0.907</td>
      <td>0.880</td>
      <td>0.775</td>
      <td>0.718</td>
      <td>0.806</td>
      <td>0.776</td>
      <td>0.726</td>
      <td>0.656</td>
      <td>0.542</td>
      <td>0.469</td>
    </tr>
    <tr>
      <th>slovnet_bert</th>
      <td><b>0.965</b></td>
      <td><b>0.936</b></td>
      <td><b>0.891</b></td>
      <td><b>0.828</b></td>
      <td><b>0.958</b></td>
      <td><b>0.940</b></td>
      <td><b>0.846</b></td>
      <td><b>0.782</b></td>
      <td><b>0.776</b></td>
      <td><b>0.706</b></td>
    </tr>
    <tr>
      <th>deeppavlov_bert</th>
      <td><b>0.962</b></td>
      <td><b>0.910</b></td>
      <td><b>0.882</b></td>
      <td><b>0.786</b></td>
      <td><b>0.963</b></td>
      <td><b>0.929</b></td>
      <td><b>0.844</b></td>
      <td><b>0.761</b></td>
      <td><b>0.784</b></td>
      <td><b>0.691</b></td>
    </tr>
    <tr>
      <th>udpipe</th>
      <td>0.873</td>
      <td>0.823</td>
      <td>0.622</td>
      <td>0.531</td>
      <td>0.910</td>
      <td>0.876</td>
      <td>0.700</td>
      <td>0.624</td>
      <td>0.625</td>
      <td>0.534</td>
    </tr>
    <tr>
      <th>spacy</th>
      <td>0.876</td>
      <td>0.818</td>
      <td>0.770</td>
      <td>0.665</td>
      <td>0.880</td>
      <td>0.833</td>
      <td>0.757</td>
      <td>0.666</td>
      <td>0.657</td>
      <td>0.544</td>
    </tr>
    <tr>
      <th>stanza</th>
      <td><b>0.940</b></td>
      <td><b>0.886</b></td>
      <td><b>0.827</b></td>
      <td><b>0.723</b></td>
      <td><b>0.936</b></td>
      <td><b>0.895</b></td>
      <td><b>0.802</b></td>
      <td><b>0.714</b></td>
      <td><b>0.713</b></td>
      <td><b>0.613</b></td>
    </tr>
  </tbody>
</table>
<!--- syntax1 --->

<!--- syntax2 --->
<table border="0" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>init, s</th>
      <th>disk, mb</th>
      <th>ram, mb</th>
      <th>speed, it/s</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>slovnet</th>
      <td><b>1.0</b></td>
      <td><b>27</b></td>
      <td><b>125</b></td>
      <td><b>450.0</b></td>
    </tr>
    <tr>
      <th>slovnet_bert</th>
      <td><b>5.0</b></td>
      <td>504</td>
      <td>3427</td>
      <td><b>200.0 (gpu)</b></td>
    </tr>
    <tr>
      <th>deeppavlov_bert</th>
      <td>34.0</td>
      <td>1427</td>
      <td>8704</td>
      <td><b>75.0 (gpu)</b></td>
    </tr>
    <tr>
      <th>udpipe</th>
      <td>6.9</td>
      <td><b>45</b></td>
      <td><b>242</b></td>
      <td>56.2</td>
    </tr>
    <tr>
      <th>spacy</th>
      <td>9.0</td>
      <td><b>89</b></td>
      <td><b>579</b></td>
      <td>41.0</td>
    </tr>
    <tr>
      <th>stanza</th>
      <td><b>3.0</b></td>
      <td>591</td>
      <td>890</td>
      <td>12.0</td>
    </tr>
  </tbody>
</table>
<!--- syntax2 --->

## NER

See <a href="https://github.com/natasha/slovnet#evaluation">Slovnet evalualtion section</a> for more info.

<!--- ner1 --->
<table border="0" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="3" halign="left">factru</th>
      <th colspan="2" halign="left">gareev</th>
      <th colspan="3" halign="left">ne5</th>
      <th colspan="3" halign="left">bsnlp</th>
    </tr>
    <tr>
      <th>f1</th>
      <th>PER</th>
      <th>LOC</th>
      <th>ORG</th>
      <th>PER</th>
      <th>ORG</th>
      <th>PER</th>
      <th>LOC</th>
      <th>ORG</th>
      <th>PER</th>
      <th>LOC</th>
      <th>ORG</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>slovnet</th>
      <td><b>0.959</b></td>
      <td><b>0.915</b></td>
      <td><b>0.825</b></td>
      <td>0.977</td>
      <td><b>0.899</b></td>
      <td>0.984</td>
      <td>0.973</td>
      <td>0.951</td>
      <td>0.944</td>
      <td>0.834</td>
      <td>0.718</td>
    </tr>
    <tr>
      <th>slovnet_bert</th>
      <td><b>0.973</b></td>
      <td><b>0.928</b></td>
      <td><b>0.831</b></td>
      <td><b>0.991</b></td>
      <td><b>0.911</b></td>
      <td><b>0.996</b></td>
      <td><b>0.989</b></td>
      <td><b>0.976</b></td>
      <td><b>0.960</b></td>
      <td>0.838</td>
      <td><b>0.733</b></td>
    </tr>
    <tr>
      <th>deeppavlov</th>
      <td>0.910</td>
      <td>0.886</td>
      <td>0.742</td>
      <td>0.944</td>
      <td>0.798</td>
      <td>0.942</td>
      <td>0.919</td>
      <td>0.881</td>
      <td>0.866</td>
      <td>0.767</td>
      <td>0.624</td>
    </tr>
    <tr>
      <th>deeppavlov_bert</th>
      <td><b>0.971</b></td>
      <td><b>0.928</b></td>
      <td><b>0.825</b></td>
      <td><b>0.980</b></td>
      <td><b>0.916</b></td>
      <td><b>0.997</b></td>
      <td><b>0.990</b></td>
      <td><b>0.976</b></td>
      <td><b>0.954</b></td>
      <td><b>0.840</b></td>
      <td><b>0.741</b></td>
    </tr>
    <tr>
      <th>deeppavlov_slavic</th>
      <td>0.956</td>
      <td>0.884</td>
      <td>0.714</td>
      <td>0.976</td>
      <td>0.776</td>
      <td>0.984</td>
      <td>0.817</td>
      <td>0.761</td>
      <td><b>0.965</b></td>
      <td><b>0.925</b></td>
      <td><b>0.831</b></td>
    </tr>
    <tr>
      <th>pullenti</th>
      <td>0.905</td>
      <td>0.814</td>
      <td>0.686</td>
      <td>0.939</td>
      <td>0.639</td>
      <td>0.952</td>
      <td>0.862</td>
      <td>0.683</td>
      <td>0.900</td>
      <td>0.769</td>
      <td>0.566</td>
    </tr>
    <tr>
      <th>spacy</th>
      <td>0.955</td>
      <td>0.914</td>
      <td>0.803</td>
      <td><b>0.980</b></td>
      <td>0.894</td>
      <td><b>0.990</b></td>
      <td><b>0.973</b></td>
      <td><b>0.951</b></td>
      <td>0.938</td>
      <td>0.828</td>
      <td>0.703</td>
    </tr>
    <tr>
      <th>stanza</th>
      <td>0.943</td>
      <td>0.865</td>
      <td>0.687</td>
      <td>0.953</td>
      <td>0.827</td>
      <td>0.923</td>
      <td>0.753</td>
      <td>0.734</td>
      <td>0.938</td>
      <td><b>0.838</b></td>
      <td>0.724</td>
    </tr>
    <tr>
      <th>texterra</th>
      <td>0.900</td>
      <td>0.800</td>
      <td>0.597</td>
      <td>0.888</td>
      <td>0.561</td>
      <td>0.901</td>
      <td>0.777</td>
      <td>0.594</td>
      <td>0.858</td>
      <td>0.783</td>
      <td>0.548</td>
    </tr>
    <tr>
      <th>tomita</th>
      <td>0.929</td>
      <td></td>
      <td></td>
      <td>0.921</td>
      <td></td>
      <td>0.945</td>
      <td></td>
      <td></td>
      <td>0.881</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>mitie</th>
      <td>0.888</td>
      <td>0.861</td>
      <td>0.532</td>
      <td>0.849</td>
      <td>0.452</td>
      <td>0.753</td>
      <td>0.642</td>
      <td>0.432</td>
      <td>0.736</td>
      <td>0.801</td>
      <td>0.524</td>
    </tr>
  </tbody>
</table>
<!--- ner1 --->

<!--- ner2 --->
<table border="0" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>init, s</th>
      <th>disk, mb</th>
      <th>ram, mb</th>
      <th>speed, it/s</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>slovnet</th>
      <td><b>1.0</b></td>
      <td><b>27</b></td>
      <td><b>205</b></td>
      <td>25.3</td>
    </tr>
    <tr>
      <th>slovnet_bert</th>
      <td>5.0</td>
      <td>473</td>
      <td>9500</td>
      <td><b>40.0 (gpu)</b></td>
    </tr>
    <tr>
      <th>deeppavlov</th>
      <td>5.9</td>
      <td>1024</td>
      <td>3072</td>
      <td>24.3 (gpu)</td>
    </tr>
    <tr>
      <th>deeppavlov_bert</th>
      <td>34.5</td>
      <td>2048</td>
      <td>6144</td>
      <td>13.1 (gpu)</td>
    </tr>
    <tr>
      <th>deeppavlov_slavic</th>
      <td>35.0</td>
      <td>2048</td>
      <td>4096</td>
      <td>8.0 (gpu)</td>
    </tr>
    <tr>
      <th>pullenti</th>
      <td><b>2.9</b></td>
      <td><b>16</b></td>
      <td><b>253</b></td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>spacy</th>
      <td>8.0</td>
      <td>89</td>
      <td>625</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>stanza</th>
      <td>3.0</td>
      <td>591</td>
      <td>11264</td>
      <td>3.0 (gpu)</td>
    </tr>
    <tr>
      <th>texterra</th>
      <td>47.6</td>
      <td>193</td>
      <td>3379</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>tomita</th>
      <td><b>2.0</b></td>
      <td><b>64</b></td>
      <td><b>63</b></td>
      <td><b>29.8</b></td>
    </tr>
    <tr>
      <th>mitie</th>
      <td>28.3</td>
      <td>327</td>
      <td>261</td>
      <td><b>32.8</b></td>
    </tr>
  </tbody>
</table>
<!--- ner2 --->

## Support

- Chat — https://telegram.me/natural_language_processing
- Issues — https://github.com/natasha/nerus/issues
- Commercial support — https://lab.alexkuk.ru
