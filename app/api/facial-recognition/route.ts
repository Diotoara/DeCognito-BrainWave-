// import path from 'path'
// import { spawn } from 'child_process'
// import { NextRequest, NextResponse } from 'next/server'

// export async function POST(request: NextRequest) {
//   try {
//     const body = await request.json()

//     const pythonScriptPath = path.join(
//       process.cwd(),
//       'backend',
//       'script',
//       'facial_runner.py'
//     )

//     const py = spawn(
//       process.platform === 'win32' ? 'python' : 'python3',
//       [pythonScriptPath]
//     )

//     let stdout = ''
//     let stderr = ''

//     py.stdin.write(JSON.stringify(body))
//     py.stdin.end()

//     py.stdout.on('data', (data) => {
//       stdout += data.toString()
//     })

//     py.stderr.on('data', (data) => {
//       stderr += data.toString()
//     })

//     return await new Promise((resolve) => {
//       py.on('close', (code) => {
//         if (code !== 0 || stderr.includes('Traceback')) {
//           console.error('Python Error:', stderr)
//           return resolve(
//             NextResponse.json({ status: 'error', error: stderr }, { status: 500 })
//           )
//         }
//         try {
//           const result = JSON.parse(stdout)
//           return resolve(NextResponse.json(result))
//         } catch (e) {
//           console.error('JSON parse error:', stdout)
//           return resolve(
//             NextResponse.json(
//               { status: 'error', error: 'Invalid JSON from Python' },
//               { status: 500 }
//             )
//           )
//         }
//       })
//     })
//   } catch (err) {
//     const msg = err instanceof Error ? err.message : 'Unknown error'
//     return NextResponse.json({ status: 'error', error: msg }, { status: 500 })
//   }
// }


// above best 


import path from 'path'
import { spawn } from 'child_process'
import { NextRequest, NextResponse } from 'next/server'

export async function POST(request: NextRequest) {
  try {
    const body = await request.json()

    const pythonScriptPath = path.join(
      process.cwd(),
      'backend',
      'script',
      'facial_runner.py'
    )

    const py = spawn(
      process.platform === 'win32' ? 'python' : 'python3',
      [pythonScriptPath]
    )

    let stdout = ''
    let stderr = ''

    py.stdin.write(JSON.stringify(body))
    py.stdin.end()

    py.stdout.on('data', (data) => {
      stdout += data.toString()
    })

    py.stderr.on('data', (data) => {
      stderr += data.toString()
    })

    return await new Promise((resolve) => {
      py.on('close', (code) => {
        if (code !== 0 || stderr.includes('Traceback')) {
          console.error('Python Error:', stderr)
          return resolve(
            NextResponse.json({ status: 'error', error: stderr }, { status: 500 })
          )
        }
        try {
          const result = JSON.parse(stdout)
          return resolve(NextResponse.json(result))
        } catch (e) {
          console.error('JSON parse error:', stdout)
          return resolve(
            NextResponse.json(
              { status: 'error', error: 'Invalid JSON from Python' },
              { status: 500 }
            )
          )
        }
      })
    })
  } catch (err) {
    const msg = err instanceof Error ? err.message : 'Unknown error'
    return NextResponse.json({ status: 'error', error: msg }, { status: 500 })
  }
}