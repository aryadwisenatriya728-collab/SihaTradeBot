content = open('server.js').read()

old = '''function createTransporter() {
  const gmailUser = process.env.GMAIL_USER;
  const gmailPass = process.env.GMAIL_PASS;
  if (!gmailUser || !gmailPass) throw new Error('GMAIL_USER atau GMAIL_PASS belum diset di environment variable.');
  return nodemailer.createTransport({
    service: 'gmail',
    auth: { user: gmailUser, pass: gmailPass }
  });
}'''

new = '''function createTransporter() {
  const gmailUser = process.env.GMAIL_USER;
  const gmailPass = process.env.GMAIL_PASS;
  if (!gmailUser || !gmailPass) throw new Error('GMAIL_USER atau GMAIL_PASS belum diset di environment variable.');
  return nodemailer.createTransport({
    host: 'smtp.gmail.com',
    port: 465,
    secure: true,
    auth: { user: gmailUser, pass: gmailPass },
    tls: { rejectUnauthorized: false }
  });
}'''

content = content.replace(old, new)
open('server.js', 'w').write(content)
print("Done")
