<img src="https://github.com/natasha/natasha-logos/blob/master/naeval.svg">

Naeval — comparing quality and performance of NLP systems for Russian language. Naeval is used to evaluate <a href="https://github.com/natasha">project Natasha</a> components: <a href="https://github.com/natasha/razdel">Razdel</a>, <a href="https://github.com/natasha/navec">Navec</a>, <a href="https://github.com/natasha/slovnet">Slovnet</a>:

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
      <td>4217</td>
      <td>0.5</td>
      <td>2914</td>
      <td>0.5</td>
      <td>2402</td>
      <td>0.3</td>
      <td>8630</td>
      <td>0.3</td>
    </tr>
    <tr>
      <th>spacy</th>
      <td>3283</td>
      <td>5.6</td>
      <td>2639</td>
      <td>5.5</td>
      <td>1742</td>
      <td>3.8</td>
      <td>4010</td>
      <td>3.5</td>
    </tr>
    <tr>
      <th>nltk.word_tokenize</th>
      <td>5712</td>
      <td>3.7</td>
      <td>67523</td>
      <td>3.9</td>
      <td>12149</td>
      <td>2.7</td>
      <td>13564</td>
      <td>2.8</td>
    </tr>
    <tr>
      <th>mystem</th>
      <td>4280</td>
      <td>4.9</td>
      <td>3624</td>
      <td>4.6</td>
      <td>2515</td>
      <td>3.6</td>
      <td><b>1812</b></td>
      <td>3.5</td>
    </tr>
    <tr>
      <th>mosestokenizer</th>
      <td><b>1188</b></td>
      <td><b>2.0</b></td>
      <td>1641</td>
      <td><b>2.1</b></td>
      <td>1696</td>
      <td><b>1.7</b></td>
      <td>2486</td>
      <td><b>1.7</b></td>
    </tr>
    <tr>
      <th>segtok.word_tokenize</th>
      <td>1491</td>
      <td><b>2.4</b></td>
      <td><b>1552</b></td>
      <td><b>2.4</b></td>
      <td><b>1657</b></td>
      <td><b>1.8</b></td>
      <td><b>1238</b></td>
      <td><b>1.8</b></td>
    </tr>
    <tr>
      <th>aatimofeev/spacy_russian_tokenizer</th>
      <td><b>1485</b></td>
      <td>56.2</td>
      <td><b>1225</b></td>
      <td>53.3</td>
      <td><b>630</b></td>
      <td>39.2</td>
      <td>2972</td>
      <td>47.6</td>
    </tr>
    <tr>
      <th>koziev/rutokenizer</th>
      <td>2744</td>
      <td><b>1.1</b></td>
      <td><b>1632</b></td>
      <td><b>1.1</b></td>
      <td>2576</td>
      <td><b>0.9</b></td>
      <td>9915</td>
      <td><b>0.9</b></td>
    </tr>
    <tr>
      <th>razdel.tokenize</th>
      <td><b>1158</b></td>
      <td>2.9</td>
      <td>1861</td>
      <td>3.0</td>
      <td><b>315</b></td>
      <td>2.0</td>
      <td><b>2264</b></td>
      <td>2.1</td>
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
      <td>19974</td>
      <td>0.7</td>
      <td>5986</td>
      <td>0.4</td>
      <td>9380</td>
      <td>0.5</td>
      <td>22483</td>
      <td>0.8</td>
    </tr>
    <tr>
      <th>segtok.split_single</th>
      <td>19450</td>
      <td>16.5</td>
      <td><b>4140</b></td>
      <td>10.3</td>
      <td>158672</td>
      <td><b>1.5</b></td>
      <td>172887</td>
      <td><b>3.1</b></td>
    </tr>
    <tr>
      <th>mosestokenizer</th>
      <td>60212</td>
      <td>10.6</td>
      <td>39361</td>
      <td><b>5.4</b></td>
      <td>12238</td>
      <td>5.7</td>
      <td>168743</td>
      <td>385.1</td>
    </tr>
    <tr>
      <th>nltk.sent_tokenize</th>
      <td><b>16346</b></td>
      <td><b>8.8</b></td>
      <td>4194</td>
      <td><b>4.3</b></td>
      <td><b>6774</b></td>
      <td><b>4.2</b></td>
      <td><b>32391</b></td>
      <td><b>5.4</b></td>
    </tr>
    <tr>
      <th>deeppavlov/rusenttokenize</th>
      <td><b>10138</b></td>
      <td><b>9.9</b></td>
      <td><b>1180</b></td>
      <td>6.0</td>
      <td><b>8402</b></td>
      <td>5.6</td>
      <td><b>20717</b></td>
      <td>93.4</td>
    </tr>
    <tr>
      <th>razdel.sentenize</th>
      <td><b>9408</b></td>
      <td><b>5.4</b></td>
      <td><b>798</b></td>
      <td><b>3.4</b></td>
      <td><b>11020</b></td>
      <td><b>3.6</b></td>
      <td><b>10791</b></td>
      <td><b>5.4</b></td>
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
      <th>deeppavlov</th>
      <td><b>0.910</b></td>
      <td><b>0.886</b></td>
      <td><b>0.742</b></td>
      <td><b>0.944</b></td>
      <td><b>0.798</b></td>
      <td>0.942</td>
      <td><b>0.919</b></td>
      <td><b>0.881</b></td>
      <td>0.866</td>
      <td>0.767</td>
      <td><b>0.624</b></td>
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
      <td><b>0.686</b></td>
      <td><b>0.939</b></td>
      <td><b>0.639</b></td>
      <td><b>0.952</b></td>
      <td><b>0.862</b></td>
      <td><b>0.683</b></td>
      <td><b>0.900</b></td>
      <td>0.769</td>
      <td><b>0.566</b></td>
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
      <td><b>0.783</b></td>
      <td>0.548</td>
    </tr>
    <tr>
      <th>tomita</th>
      <td><b>0.929</b></td>
      <td></td>
      <td></td>
      <td>0.921</td>
      <td></td>
      <td><b>0.945</b></td>
      <td></td>
      <td></td>
      <td><b>0.881</b></td>
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
      <td><b>0.861</b></td>
      <td>0.532</td>
      <td>0.849</td>
      <td>0.452</td>
      <td>0.753</td>
      <td>0.642</td>
      <td>0.432</td>
      <td>0.736</td>
      <td><b>0.801</b></td>
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
      <th>speed, articles/s</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>deeppavlov</th>
      <td>5.9</td>
      <td>1024</td>
      <td>3072</td>
      <td><b>24.3 (gpu)</b></td>
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
      <td><b>2.9</b></td>
      <td><b>16</b></td>
      <td><b>253</b></td>
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
      <td><b>64</b></td>
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
