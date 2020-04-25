<img src="https://github.com/natasha/natasha-logos/blob/master/naeval.svg">

Naeval — comparing quality and performance of NLP systems for Russian language. Naeval is used to evaluate <a href="https://github.com/natasha">project Natasha</a> components: <a href="https://github.com/natasha/razdel">Razdel</a>, <a href="https://github.com/natasha/navec">Navec</a>, <a href="https://github.com/natasha/slovnet">Slovnet</a>:

## Tokenization

See <a href="https://github.com/natasha/razdel#quality-performance">Razdel evalualtion section</a> for more info.

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
      <td>4161</td>
      <td>0.5</td>
      <td>2660</td>
      <td>0.5</td>
      <td>2277</td>
      <td>0.4</td>
      <td>7606</td>
      <td>0.4</td>
    </tr>
    <tr>
      <th>spacy</th>
      <td>4388</td>
      <td>6.2</td>
      <td>2103</td>
      <td>5.8</td>
      <td><b>1740</b></td>
      <td>4.1</td>
      <td>4057</td>
      <td>3.9</td>
    </tr>
    <tr>
      <th>nltk.word_tokenize</th>
      <td>14245</td>
      <td>3.4</td>
      <td>60893</td>
      <td>3.3</td>
      <td>13496</td>
      <td>2.7</td>
      <td>41485</td>
      <td>2.9</td>
    </tr>
    <tr>
      <th>mystem</th>
      <td>4514</td>
      <td>5.0</td>
      <td>3153</td>
      <td>4.7</td>
      <td>2497</td>
      <td>3.7</td>
      <td><b>2028</b></td>
      <td>3.9</td>
    </tr>
    <tr>
      <th>mosestokenizer</th>
      <td><b>1886</b></td>
      <td><b>2.1</b></td>
      <td><b>1330</b></td>
      <td><b>1.9</b></td>
      <td>1796</td>
      <td><b>1.6</b></td>
      <td><b>2123</b></td>
      <td><b>1.7</b></td>
    </tr>
    <tr>
      <th>segtok.word_tokenize</th>
      <td>2772</td>
      <td><b>2.3</b></td>
      <td><b>1288</b></td>
      <td><b>2.3</b></td>
      <td>1759</td>
      <td><b>1.8</b></td>
      <td><b>1229</b></td>
      <td><b>1.8</b></td>
    </tr>
    <tr>
      <th>aatimofeev/spacy_russian_tokenizer</th>
      <td>2930</td>
      <td>48.7</td>
      <td><b>719</b></td>
      <td>51.1</td>
      <td><b>678</b></td>
      <td>39.5</td>
      <td>2681</td>
      <td>52.2</td>
    </tr>
    <tr>
      <th>koziev/rutokenizer</th>
      <td><b>2627</b></td>
      <td><b>1.1</b></td>
      <td>1386</td>
      <td><b>1.0</b></td>
      <td>2893</td>
      <td><b>0.8</b></td>
      <td>9411</td>
      <td><b>0.9</b></td>
    </tr>
    <tr>
      <th>razdel.tokenize</th>
      <td><b>1510</b></td>
      <td>2.9</td>
      <td>1483</td>
      <td>2.8</td>
      <td><b>322</b></td>
      <td>2.0</td>
      <td>2124</td>
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
      <td>20456</td>
      <td>0.9</td>
      <td>6576</td>
      <td>0.6</td>
      <td>10084</td>
      <td>0.7</td>
      <td>23356</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>segtok.split_single</th>
      <td>19008</td>
      <td>17.8</td>
      <td>4422</td>
      <td>13.4</td>
      <td>159738</td>
      <td><b>1.1</b></td>
      <td>164218</td>
      <td><b>2.8</b></td>
    </tr>
    <tr>
      <th>mosestokenizer</th>
      <td>41666</td>
      <td><b>8.9</b></td>
      <td>22082</td>
      <td><b>5.7</b></td>
      <td>12663</td>
      <td>6.4</td>
      <td>50560</td>
      <td><b>7.4</b></td>
    </tr>
    <tr>
      <th>nltk.sent_tokenize</th>
      <td><b>16420</b></td>
      <td><b>10.1</b></td>
      <td><b>4350</b></td>
      <td><b>5.3</b></td>
      <td><b>7074</b></td>
      <td><b>5.6</b></td>
      <td><b>32534</b></td>
      <td>8.9</td>
    </tr>
    <tr>
      <th>deeppavlov/rusenttokenize</th>
      <td><b>10192</b></td>
      <td>10.9</td>
      <td><b>1210</b></td>
      <td>7.9</td>
      <td><b>8910</b></td>
      <td>6.8</td>
      <td><b>21410</b></td>
      <td><b>7.0</b></td>
    </tr>
    <tr>
      <th>razdel.sentenize</th>
      <td><b>9274</b></td>
      <td><b>6.1</b></td>
      <td><b>824</b></td>
      <td><b>3.9</b></td>
      <td><b>11414</b></td>
      <td><b>4.5</b></td>
      <td><b>10594</b></td>
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
  </tbody>
</table>
<!--- emb2 --->

## Morphology taggers

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
      <th>rupostagger</th>
      <td>0.673</td>
      <td>0.645</td>
      <td>0.661</td>
      <td>0.641</td>
      <td>0.636</td>
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
      <th>udpipe</th>
      <td>0.918</td>
      <td>0.811</td>
      <td><b>0.957</b></td>
      <td><b>0.870</b></td>
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
      <th>rupostagger</th>
      <td><b>4.8</b></td>
      <td><b>3</b></td>
      <td><b>118</b></td>
      <td>48.0</td>
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
      <th>udpipe</th>
      <td>6.9</td>
      <td>45</td>
      <td><b>242</b></td>
      <td>56.2</td>
    </tr>
    <tr>
      <th>spacy</th>
      <td>10.9</td>
      <td>89</td>
      <td>579</td>
      <td>30.6</td>
    </tr>
    <tr>
      <th>deeppavlov</th>
      <td><b>4.0</b></td>
      <td>32</td>
      <td>10240</td>
      <td><b>90.0 (gpu)</b></td>
    </tr>
    <tr>
      <th>deeppavlov_bert</th>
      <td>20.0</td>
      <td>1393</td>
      <td>8704</td>
      <td>85.0 (gpu)</td>
    </tr>
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
      <th>udpipe</th>
      <td>0.873</td>
      <td>0.823</td>
      <td>0.622</td>
      <td>0.531</td>
      <td><b>0.910</b></td>
      <td><b>0.876</b></td>
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
      <td><b>0.757</b></td>
      <td><b>0.666</b></td>
      <td><b>0.657</b></td>
      <td><b>0.544</b></td>
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
      <th>slovnet</th>
      <td><b>0.907</b></td>
      <td><b>0.880</b></td>
      <td><b>0.775</b></td>
      <td><b>0.718</b></td>
      <td>0.806</td>
      <td>0.776</td>
      <td>0.726</td>
      <td>0.656</td>
      <td>0.542</td>
      <td>0.469</td>
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
      <th>udpipe</th>
      <td><b>6.9</b></td>
      <td><b>45</b></td>
      <td><b>242</b></td>
      <td>56.2</td>
    </tr>
    <tr>
      <th>spacy</th>
      <td>10.9</td>
      <td><b>89</b></td>
      <td><b>579</b></td>
      <td>31.6</td>
    </tr>
    <tr>
      <th>deeppavlov_bert</th>
      <td>34.0</td>
      <td>1427</td>
      <td>8704</td>
      <td><b>75.0 (gpu)</b></td>
    </tr>
    <tr>
      <th>slovnet_bert</th>
      <td><b>5.0</b></td>
      <td>504</td>
      <td>3427</td>
      <td><b>200.0 (gpu)</b></td>
    </tr>
    <tr>
      <th>slovnet</th>
      <td><b>1.0</b></td>
      <td><b>27</b></td>
      <td><b>125</b></td>
      <td><b>450.0</b></td>
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
      <td><b>0.838</b></td>
      <td><b>0.733</b></td>
    </tr>
    <tr>
      <th>slovnet</th>
      <td><b>0.959</b></td>
      <td><b>0.915</b></td>
      <td><b>0.825</b></td>
      <td><b>0.977</b></td>
      <td><b>0.899</b></td>
      <td><b>0.984</b></td>
      <td><b>0.973</b></td>
      <td><b>0.951</b></td>
      <td><b>0.944</b></td>
      <td><b>0.834</b></td>
      <td><b>0.718</b></td>
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
      <th>natasha</th>
      <td>0.867</td>
      <td>0.753</td>
      <td>0.297</td>
      <td>0.873</td>
      <td>0.347</td>
      <td>0.852</td>
      <td>0.709</td>
      <td>0.394</td>
      <td>0.836</td>
      <td>0.755</td>
      <td>0.350</td>
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
      <th>slovnet_bert</th>
      <td>5.0</td>
      <td>473</td>
      <td>9500</td>
      <td><b>40.0 (gpu)</b></td>
    </tr>
    <tr>
      <th>slovnet</th>
      <td><b>1.0</b></td>
      <td><b>27</b></td>
      <td><b>205</b></td>
      <td>25.3</td>
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
      <th>pullenti</th>
      <td>2.9</td>
      <td><b>16</b></td>
      <td>253</td>
      <td>6.0</td>
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
      <td>64</td>
      <td><b>63</b></td>
      <td><b>29.8</b></td>
    </tr>
    <tr>
      <th>natasha</th>
      <td><b>2.0</b></td>
      <td><b>1</b></td>
      <td><b>160</b></td>
      <td>8.8</td>
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
