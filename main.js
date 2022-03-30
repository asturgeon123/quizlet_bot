// Modules to control application life and create native browser window
const {app, BrowserWindow,autoUpdater, dialog } = require('electron')

const path = require('path')
require('update-electron-app')()


function createWindow () {

  let backend;
  //backend = path.join(process.cwd(), '/dist/app.exe')
  backend = path.join(process.cwd(), 'resources/app/dist/app.exe')
  var execfile = require('child_process').execFile;
  execfile(
   backend,
   {
    windowsHide: true,
   },
   (err, stdout, stderr) => {
    if (err) {
    console.log(err);
    }
    if (stdout) {
    console.log(stdout);
    }
    if (stderr) {
    console.log(stderr);
    }
   }
  )



  // Create the browser window.
  const mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js')
    }
  })

  // and load the index.html of the app.
  mainWindow.loadURL("http://localhost:5000");


  // Open the DevTools.
  // mainWindow.webContents.openDevTools()
}

// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
// Some APIs can only be used after this event occurs.
app.whenReady().then(() => {
  createWindow()

  app.on('activate', function () {
    // On macOS it's common to re-create a window in the app when the
    // dock icon is clicked and there are no other windows open.
    if (BrowserWindow.getAllWindows().length === 0) createWindow()
  })
})

// Quit when all windows are closed, except on macOS. There, it's common
// for applications and their menu bar to stay active until the user quits
// explicitly with Cmd + Q.
app.on('window-all-closed', function () {
  const { exec } = require('child_process');

  exec('taskkill /f /t /im app.exe', (err, stdout, stderr) => {
  if (err) {
    console.log(err)
  return;
  }
  console.log(`stdout: ${stdout}`);
  console.log(`stderr: ${stderr}`);
  });


  if (process.platform !== 'darwin') app.quit()
})

// In this file you can include the rest of your app's specific main process
// code. You can also put them in separate files and require them here.