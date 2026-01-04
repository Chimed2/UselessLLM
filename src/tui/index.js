const blessed = require('blessed');
const { spawn } = require('child_process');
const path = require('path');

const screen = blessed.screen({
  smartCSR: true,
  title: 'UselessLLM'
});

const container = blessed.box({
  top: 'center',
  left: 'center',
  width: '100%',
  height: '100%',
  content: '',
  tags: true,
  style: {
    fg: 'green',
    bg: 'black'
  }
});

screen.append(container);

const logo = blessed.text({
  parent: container,
  top: 1,
  left: 'center',
  content: '> UselessLLM',
  style: {
    fg: 'green',
    bold: true
  }
});

const outputBox = blessed.box({
  parent: container,
  top: 3,
  left: 'center',
  width: '90%',
  height: '60%',
  label: ' System Output ',
  content: 'System initialized. Resources being wasted idle.',
  tags: true,
  border: {
    type: 'line'
  },
  style: {
    fg: 'green',
    border: {
      fg: 'green'
    }
  }
});

const inputBox = blessed.textbox({
  parent: container,
  bottom: 2,
  left: 'center',
  width: '90%',
  height: 3,
  label: ' Input ',
  inputOnFocus: true,
  border: {
    type: 'line'
  },
  style: {
    fg: 'white',
    border: {
      fg: 'yellow'
    }
  }
});

inputBox.key('enter', function(ch, key) {
  const query = this.getValue();
  this.clearValue();
  this.focus();
  
  outputBox.setContent('{center}Processing... (Inefficiently){/center}');
  screen.render();

  const pythonScript = path.join(__dirname, '../backend/logic.py');
  const pythonProcess = spawn('python3', [pythonScript, query]);

  let result = '';

  pythonProcess.stdout.on('data', (data) => {
    result += data.toString();
  });

  pythonProcess.stderr.on('data', (data) => {
      result += " [Error generating nonsense]";
  });

  pythonProcess.on('close', (code) => {
    outputBox.setContent(result);
    screen.render();
  });
});

screen.key(['escape', 'q', 'C-c'], function(ch, key) {
  return process.exit(0);
});

inputBox.focus();
screen.render();
