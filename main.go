package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
	"os/exec"
)

func uploadFile(w http.ResponseWriter, r *http.Request) {
	fmt.Println("File Upload Endpoint Hit")

	// Parse our multipart form, 10 << 20 specifies a maximum
	// upload of 10 MB files.
	r.ParseMultipartForm(10 << 20)

	// FormFile returns the first file for the given key `myFile`
	// it also returns the FileHeader so we can get the Filename,
	// the Header, and the size of the file
	file, handler, err := r.FormFile("myFile")
	if err != nil {
		fmt.Println("Error Retrieving the File")
		fmt.Println(err)
		return
	}
	defer file.Close()

	fmt.Printf("Uploaded File: %+v\n", handler.Filename)
	fmt.Printf("File Size: %+v\n", handler.Size)
	fmt.Printf("MIME Header: %+v\n", handler.Header)

	// Create a temporary file within our temp-images directory that follows
	// a particular naming pattern
	tempFile, err := ioutil.TempFile("temp-images", "upload-*.png")
	if err != nil {
		fmt.Println(err)
	}
	defer tempFile.Close()

	// read all of the contents of our uploaded file into a
	// byte array
	fileBytes, err := ioutil.ReadAll(file)
	if err != nil {
		fmt.Println(err)
	}

	// write this byte array to our temporary file
	tempFile.Write(fileBytes)

	// Execute the Bash script
	cmd := exec.Command("bash", "script.sh", tempFile.Name())
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr

	err = cmd.Run()
	if err != nil {
		fmt.Println("Error executing script:", err)
	}

	// return that we have successfully uploaded our file!
	fmt.Fprintf(w, "Successfully Uploaded File\n")
}

func setupRoutes() {
	http.HandleFunc("/upload", uploadFile)
	http.HandleFunc("/trigger_open_html", openHTMLHandler)
	http.ListenAndServe(":8080", nil)
}
func openHTMLHandler(w http.ResponseWriter, r *http.Request) {
	// Check if HTML file opening is requested

	// Replace "your_html_file.html" with the actual path to your HTML file
	htmlFilePath := "display.html"

	// Open the HTML file in the default web browser
	cmd := exec.Command("open", htmlFilePath)
	err := cmd.Run()
	if err != nil {
		fmt.Fprintf(w, "Error opening HTML file: %v", err)
		return
	}

	fmt.Fprintf(w, "HTML file opened successfully!")

	// Reset the flag after handling the request

}

func main() {
	fmt.Println("Hello World")
	setupRoutes()
}
