numToURL = [
    'https://static.wixstatic.com/media/7ab48f_805fea4b735645558a93b6b9b41ea690~mv2.png',
    'https://static.wixstatic.com/media/7ab48f_03be95aecff04e0689b56eff5fd22165~mv2.png',
    'https://static.wixstatic.com/media/7ab48f_a5944e998d9447f883e3679351f3019d~mv2.png',
    'https://static.wixstatic.com/media/7ab48f_adbeecd67cf64bb198a4721ca36d807d~mv2.png',
    'https://static.wixstatic.com/media/7ab48f_5d56d3ccd3714192a46b62328e303d08~mv2.png',
    'https://static.wixstatic.com/media/7ab48f_533a776f35494d4ea82d913f62bf0368~mv2.png',
    'https://static.wixstatic.com/media/7ab48f_8f83e8453a614023b679dbcf7b9927bd~mv2.png'
]
function emoticon() {
    randomIndex=Math.floor(Math.random(0)*numToURL.length);
    img = document.getElementById('emoticon');
    url = numToURL[randomIndex];
    console.log(url);
    img.src=url;
}
emoticon()