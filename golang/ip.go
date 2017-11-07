package main

import (
	"fmt"
	"io/ioutil"
	"net"
	"net/http"
	"os"
	"regexp"
	"strings"
	"time"

	"github.com/PuerkitoBio/goquery"
	"github.com/axgle/mahonia"
)

func ip138(ip string) {
	ip138_url := "http://www.ip138.com/ips1388.asp?ip=" + ip + "&action=2"
	client := &http.Client{Timeout: 5 * time.Second}

	req, err := http.NewRequest("GET", ip138_url, nil)
	req.Header.Set("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.87 Safari/537.36")
	if err != nil {
		fmt.Println(err)
	}

	res, err := client.Do(req)
	if err != nil {
		fmt.Println(err)
	}
	defer res.Body.Close()

	/*
		把gb2312编码转成utf8编码字符串, 这里遇到了一个坑
		就是使用https://github.com/djimenez/iconv-go的时
		候, 转码后的内容会无故减少, 所以这里使用mahonia
	*/

	body_reader_gbk, _ := ioutil.ReadAll(res.Body)
	utf8_body := mahonia.NewDecoder("gbk").ConvertString(string(body_reader_gbk))
	body_reader_utf8 := strings.NewReader(utf8_body)

	//最后把string转成io reader后传递给goquery
	doc, err := goquery.NewDocumentFromReader(body_reader_utf8)
	if err != nil {
		fmt.Println(err)
	}

	fmt.Println("********************ip138********************")

	doc.Find("body > table > tbody > tr:nth-child(3) > td > ul > li").Each(func(index int, selection *goquery.Selection) {
		result, _ := selection.Html()
		fmt.Println(result)
	})
}

func ipcn(ip string) {
	ipcn_url := "http://ip.cn/index.php?ip=" + ip
	client := &http.Client{Timeout: 5 * time.Second}

	req, err := http.NewRequest("GET", ipcn_url, nil)
	req.Header.Set("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.87 Safari/537.36")
	if err != nil {
		fmt.Println(err)
		os.Exit(250)
	}

	res, err := client.Do(req)
	if err != nil {
		fmt.Println(err)
		os.Exit(250)
	}
	defer res.Body.Close()

	doc, err := goquery.NewDocumentFromResponse(res)
	if err != nil {
		fmt.Println(err)
		os.Exit(250)
	}

	fmt.Println("********************ip.cn********************")

	doc.Find("#result > div > p").Each(func(index int, selection *goquery.Selection) {
		result := selection.Text()
		fmt.Println(result)
	})

}

func main() {
	if len(os.Args) <= 1 {
		fmt.Println("Usage: ip [ip / host]")
		os.Exit(250)
	}

	ip := os.Args[1]

	match, _ := regexp.MatchString(`\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}`, ip)

	if match {
		ipcn(ip)
		ip138(ip)
	} else {
		ip, _ := net.LookupIP(os.Args[1])
		ipcn(ip[0].String())
		ip138(ip[0].String())
	}

}
